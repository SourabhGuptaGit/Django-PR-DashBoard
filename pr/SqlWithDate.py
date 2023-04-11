import pandas as pd
from datetime import date, timedelta, datetime
# from DB_agent import readDB, writeDB
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://PR:People_123$%@localhost/testdb_copy"
                        .format(user="root",
                                pw="People_123$%",
                                db="pandas"))

def writeDB(df, project_name : str):

    global engine
    project_name = project_name.lower()
    project_name = f"pr_{project_name}"
    sql_var = df.to_sql(con=engine, name=project_name, if_exists='replace')
    
    return bool(sql_var)


def readDB(project_name : str):

    global engine
    project_name = project_name.lower()
    df = pd.read_sql_query(f'select * from {project_name}', con=engine).set_index(['index'])
    
    return df




def PR_btw_Dates(Repo_name, fromdate, todate):

    #  Read Global Excels to count new entries.
    df = readDB(f"pr_global_{Repo_name}")
    data = df[(df.Date_Time <= todate) & (df.Date_Time >= fromdate)]
    # Get all User names.
    id_list = list(data['Developer_Email_ID'].unique())
    emp = []
    for i in id_list:

        ###print(f"\n🔶🔶🔸🔸🔸 Process Started for User : {i} for Repo {Repo_name}")
        i_df = data[data['Developer_Email_ID'] == i] # Data frame for one user name with "i" as variable user.
        ###print(f"    >>>  Total entries are -->  {len(i_df)} ....")

        Open_df = i_df[i_df['Status'] == 'OPEN']
        Merge_df = i_df[i_df['Status'] == 'MERGED']
        Declined_df = i_df[i_df['Status'] == 'DECLINED']

        Merge_count = len(Merge_df)
        Declined_count = len(Declined_df)
        Open_df_count = len(Open_df) # Open PR at the time of script running.
        Open_count = len(Open_df) + Declined_count + Merge_count # Open count is the total number of PR's open by the person which are merged, decliened or still open combine.

        open_min_df = Open_df[Open_df.groupby('Developer_Email_ID')['Date_Time'].transform('max') == Open_df['Date_Time']] # DataFrame of Last open PR.
        merge_max_df = Merge_df[Merge_df.groupby('Developer_Email_ID')['Date_Time'].transform('max') == Merge_df['Date_Time']] # DataFrame of Last merge PR.
        declined_max_df = Declined_df[Declined_df.groupby('Developer_Email_ID')['Date_Time'].transform('max') == Declined_df['Date_Time']] # DataFrame of Last declined PR.

        if Open_df_count != 0: # Open PR at the time of script running can not be zero to run this func.
            open_min_date = open_min_df['Date_Time'].iloc[0]
            weekdays_of_Open_PR = str(WeekdaysCount(open_min_date))
            ###print(f"    🥇  This is Open PR Table\n {Open_df}")
            ###print(f"    ******  This is First Open PR date -->  {open_min_date}   ******")
            ###print(f"    🌓  Ages of Open PR -->  {weekdays_of_Open_PR} ")
        else:
            open_min_date = "None"
            weekdays_of_Open_PR = "None"
        
        if Merge_count != 0:
            merge_max_date = merge_max_df['Date_Time'].iloc[0]
            merge_last_branch = merge_max_df['Merge Branch'].iloc[0]
            weekdays_of_merge_PR = str(WeekdaysCount(merge_max_date))
            ###print(f"    🥈  This is Merge PR Table\n {Merge_df}")
            ###print(f"    ******  This is Last Merge PR date -->  {merge_max_date}   ******")
            ###print(f"    ******  This is Last Merge PR Branch -->  {merge_last_branch}   ******")
            ###print(f"    🌓  Ages of Close PR -->  {weekdays_of_merge_PR} ")
        else:
            merge_max_date =  "None"
            merge_last_branch = "None"
            weekdays_of_merge_PR = "None"

        if Declined_count != 0:
            declined_max_date = declined_max_df['Date_Time'].iloc[0]
            ###print(f"    🥉  This is Declined PR Table\n {Declined_df}")
            ###print(f"    ******  This is Last Declined PR Date -->  {declined_max_date}   ******")
        else:
            declined_max_date =  "None"

        structure = {
            'Developer_Email_ID' : i,
            'Repo' : Repo_name,
            'Last_Merge_Branch' : merge_last_branch,
            'Current_Open_PR' : Open_df_count,
            'Open_PR' : Open_count,
            'Merged_PR' : Merge_count,
            'Declined_PR' : Declined_count,
            'Open_PR_DateTime' : open_min_date,
            'Close_PR_DateTime' : merge_max_date,
            'Declined_PR_DateTime' : declined_max_date,
            "Ages_of_Open_PR" : f"{weekdays_of_Open_PR}",
            "Ages_of_Close_PR" : f"{weekdays_of_merge_PR}"
            
        }

        emp.append(structure)
        ###print(f"🔶🔶🔸🔸🔸 Process Ends for User : {i} \n")

    df = pd.DataFrame(emp)
    if len(df) != 0:
        writeDB(df, str(f"search_btw_dates"))
        return True
    else:
        return False


def WeekdaysCount(d1 : str):

    d1 = str(d1).split(' ')[0] # Remove time from date.
    d1 = datetime.strptime(d1, "%Y-%m-%d") # first Open or last close date.
    d2 = datetime.strptime(str(date.today()), "%Y-%m-%d") # Todays Date.
    workdays = 0
    for i in range((d2 - d1).days):
        if (d1 + timedelta(days=i)).isoweekday() <= 5:
            workdays += 1

    return workdays
