from datetime import date
from django.shortcuts import render
from pr.SqlWithDate import PR_btw_Dates
from .models import *


# Create your views here.
def home(request):
    return render(request, 'OnePage/index.html', {})

def hmicsandbox(request):

    if request.method=='POST':
        try:
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("HmicSandBox", fromdate, todate)
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

def fcc(request):

    if request.method=='POST':
        try:
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("FCC", fromdate, todate)
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
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("RCC", fromdate, todate)
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
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            fromdate = fromdate if fromdate else "2019-10-30"
            todate = todate if todate else str(date.today())
            print(f'from date : {fromdate}, to date : {todate}')
            # Date_search_results = HmicSandBox.objects.raw('select * from testdb_copy.pr_hmicsandbox where Close_PR_DateTime between "'+fromdate+'" and "'+todate+'"')
            status = PR_btw_Dates("RtosApps", fromdate, todate)
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
            print("going good")
            Searched = request.POST['Searched']
            all_repo = ALL_Repo.objects.filter(Developer_Email_ID__contains=Searched)
            return render(request, 'Repos/allsearch.html', {
                'RSearched' : Searched,
                'R_all_repo' : all_repo
            })
        else:

            return render(request, 'Repos/allsearch.html', {})
    except Exception as e:
        print(e)

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