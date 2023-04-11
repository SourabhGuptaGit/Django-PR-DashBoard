import csv
import time
import xlwt
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from pr.SqlWithDate import PR_btw_Dates
from .models import *


# Create your views here.
def home(request):
    return render(request, 'OnePage/index.html', {})

def searched_btw_dates(request):

    try:
        if request.method=='POST':
            val = str(request).split("/")[1] # Not working in this case.....
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            print(f'Repo name : {val.capitalize()}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates(val.capitalize(), fromdate, todate)
            if status:
                Date_search_results = Search_btw_Dates.objects.all()
            else:
                Date_search_results = False
            return render(request, 'Repos/DatesSearch.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate, 'repo_name' : val.capitalize()})

        else:    
            return render(request, 'OnePage/index.html', {})
    except Exception as e:
        print(e)

def hmicsandbox(request):

    try:
        if request.method=='POST':
            try:
                # val = str(request).split("/")
                fromdate = request.POST.get('fromdate')
                todate = request.POST.get('todate')
                fromdate = fromdate if fromdate else "2019-10-30"
                todate = todate if todate else str(date.today())
                print(f'from date : {fromdate}, to date : {todate}')
                # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
                status = PR_btw_Dates("hmicsandbox", fromdate, todate)
                if status:
                    Date_search_results = Search_btw_Dates.objects.all()
                else:
                    Date_search_results = False
                return render(request, 'Repos/hmicsandbox.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate})
            except Exception as e:
                print(e)
        else:    
            All_Data_list = HmicSandBox.objects.all()
            return render(request, 'Repos/hmicsandbox.html', {
                'RAll_Data_list' : All_Data_list
            })
    except Exception as e:
        print(e)

def fcc(request):

    if request.method=='POST':
        try:
            val = str(request).split("/")
            print(val[1])
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("fcc", fromdate, todate)
            if status:
                Date_search_results = Search_btw_Dates.objects.all()
            else:
                Date_search_results = False
            return render(request, 'Repos/fcc.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate})
        except Exception as e:
            print(e)
    else:    
        All_Data_list = FCC.objects.all()
        return render(request, 'Repos/fcc.html', {
            'RAll_Data_list' : All_Data_list
        })

def rcc(request):

    if request.method=='POST':
        try:
            val = str(request).split("/")
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("rcc", fromdate, todate)
            if status:
                Date_search_results = Search_btw_Dates.objects.all()
            else:
                Date_search_results = False
            return render(request, 'Repos/rcc.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate})
        except Exception as e:
            print(e)
    else:    
        All_Data_list = RCC.objects.all()
        return render(request, 'Repos/rcc.html', {
            'RAll_Data_list' : All_Data_list
        })

def rtosapps(request):

    if request.method=='POST':
        try:
            val = str(request).split("/")
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("rtosapps", fromdate, todate)
            if status:
                Date_search_results = Search_btw_Dates.objects.all()
            else:
                Date_search_results = False
            return render(request, 'Repos/rtosapps.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate})
        except Exception as e:
            print(e)
    else:    
        All_Data_list = Rtosapps.objects.all()
        return render(request, 'Repos/rtosapps.html', {
            'RAll_Data_list' : All_Data_list
        })

def searched(request):
    try:
        if request.method == 'POST':
            Searched = request.POST['Searched']
            print(Searched)
            all_repo = ALL_Repo.objects.filter(Developer_Email_ID__contains=Searched)
            return render(request, 'Repos/allsearch.html', {
                'RSearched' : Searched,
                'R_all_repo' : all_repo
            })
        else:

            return render(request, 'Repos/allsearch.html', {})
    except Exception as e:
        print(e)


def csv_search_btw_dates(request):


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=PR.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	All_Data_list = Search_btw_Dates.objects.all()

	# Add column headings to the csv file
	writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

	# Loop Thu and output
	for row in All_Data_list:
		writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

	return response

def csv_repos(request):

    # if request:
    val = str(request).split("/")[1]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename=PR_{val.capitalize()}.csv'
    
    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    if val == "hmicsandbox":
        All_Data_list = HmicSandBox.objects.all()
    elif val == "fcc":
        All_Data_list = FCC.objects.all()
    elif val == "rcc":
        All_Data_list = RCC.objects.all()
    elif val == "rtosapps":
        All_Data_list = Rtosapps.objects.all()

    # Add column headings to the csv file
    writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

    # Loop Thu and output
    for row in All_Data_list:
        writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

    return response

"""
def csv_hmicsandbox(request):


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=PR.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	All_Data_list = HmicSandBox.objects.all()

	# Add column headings to the csv file
	writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

	# Loop Thu and output
	for row in All_Data_list:
		writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

	return response

def csv_fcc(request):


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=PR.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	All_Data_list = FCC.objects.all()

	# Add column headings to the csv file
	writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

	# Loop Thu and output
	for row in All_Data_list:
		writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

	return response

def csv_rcc(request):


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=PR.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	All_Data_list = RCC.objects.all()

	# Add column headings to the csv file
	writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

	# Loop Thu and output
	for row in All_Data_list:
		writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

	return response

def csv_rtosapps(request):


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=PR.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	All_Data_list = Rtosapps.objects.all()

	# Add column headings to the csv file
	writer.writerow(['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR'])

	# Loop Thu and output
	for row in All_Data_list:
		writer.writerow([row.index, row.Developer_Email_ID, row.Repo, row.Last_Merge_Branch, row.Current_Open_PR, row.Open_PR, row.Merged_PR, row.Declined_PR, row.Open_PR_DateTime, row.Close_PR_DateTime, row.Declined_PR_DateTime, row.Ages_of_Open_PR, row.Ages_of_Close_PR])

	return response

"""# def excel_search_btw_dates(request):
# 	response = HttpResponse(content_type='application/ms-excel')
# 	response['Content-Disposition'] = 'attachment; filename=Pull_Request.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws=wb.add_sheet('Sheet1')
#     row_num = 0
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     column =['index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR']
#     for col_num in range(len(column)):
#         ws.write(row_num, col_num, column[col_num], font_style)

#     font_style = xlwt.XFStyle()
#     rows = Search_btw_Dates.objects.values_list('index', 'Developer_Email_ID', 'Repo', 'Last_Merge_Branch', 'Current_Open_PR', 'Open_PR', 'Merged_PR', 'Declined_PR', 'Open_PR_DateTime', 'Close_PR_DateTime', 'Declined_PR_DateTime', 'Ages_of_Open_PR', 'Ages_of_Close_PR')

#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, str(row[col_num]), font_style)

#     wb.save(response)

#     return response



""" -----------------------------------------------------------NOT Using----------------------------------------------------------- """

def search_hmicsandbox(request):

    if request.method == 'POST':
        Searched = request.POST['Searched']
        hmicsandbox = HmicSandBox.objects.filter(Developer_Email_ID__contains=Searched)
        return render(request, 'Repos/allsearch.html', {
            'RSearched' : Searched,
            'Rhmicsandbox' : hmicsandbox
        })
    else:

        return render(request, 'Repos/search_hmicsandbox.html', {})

def search_FCC(request):

    if request.method == 'POST':
        Searched = request.POST['Searched']
        fcc = FCC.objects.filter(Developer_Email_ID__contains=Searched)
        return render(request, 'Repos/search_fcc.html', {
            'RSearched' : Searched,
            'Rfcc' : fcc
        })
    else:

        return render(request, 'Repos/search_fcc.html', {})

def search_RCC(request):

    if request.method == 'POST':
        Searched = request.POST['Searched']
        rcc = RCC.objects.filter(Developer_Email_ID__contains=Searched)
        return render(request, 'Repos/search_rcc.html', {
            'RSearched' : Searched,
            'Rrcc' : rcc
        })
    else:

        return render(request, 'Repos/search_rcc.html', {})

def search_RtosApps(request):

    if request.method == 'POST':
        Searched = request.POST['Searched']
        rtosapp = Rtosapps.objects.filter(Developer_Email_ID__contains=Searched)
        return render(request, 'Repos/search_rtosapps.html', {
            'RSearched' : Searched,
            'Rrtosapp' : rtosapp
        })
    else:

        return render(request, 'Repos/search_rtosapps.html', {})





# def test(request):
#     try:
#         if request.method=='POST':
#             try:
#                 fromdate = request.POST.get('fromdate')
#                 todate = request.POST.get('todate')
#                 fromdate = fromdate if fromdate else "2019-10-30"
#                 todate = todate if todate else str(date.today())
#                 print(f'from date : {fromdate}, to date : {todate}')
#                 # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
#                 status = PR_btw_Dates("HmicSandBox", fromdate, todate)
#                 if status:
#                     Date_search_results = Search_btw_Dates.objects.all()
#                 else:
#                     Date_search_results = False
#                 return render(request, 'Repos/Testtable.html', {'RAll_Data_list' : Date_search_results, 'from' : fromdate, 'to' : todate})
#             except Exception as e:
#                 print(e)
#         else:    
#             All_Data_list = HmicSandBox.objects.all()
#             return render(request, 'Repos/Testtable.html', {
#                 'RAll_Data_list' : All_Data_list
#             })
#     except Exception as e:
#         print(e)