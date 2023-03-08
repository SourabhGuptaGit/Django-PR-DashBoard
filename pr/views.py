from django.shortcuts import render
from .models import *


# def error_404_view(request, exception):
#     return render(request,'404.html', {})


# Create your views here.
def home(request):
    return render(request, 'OnePage/index.html', {})

def hmicsandbox(request):
    All_Data_list = HmicSandBox.objects.all()
    return render(request, 'Repos/hmicsandbox.html', {
        'RAll_Data_list' : All_Data_list
    })

def fcc(request):
    All_Data_list = FCC.objects.all()
    return render(request, 'Repos/fcc.html', {
        'RAll_Data_list' : All_Data_list
    })

def rcc(request):
    All_Data_list = RCC.objects.all()
    return render(request, 'Repos/rcc.html', {
        'RAll_Data_list' : All_Data_list
    })

def rtosapps(request):
    All_Data_list = Rtosapps.objects.all()
    return render(request, 'Repos/rtosapps.html', {
        'RAll_Data_list' : All_Data_list
    })

def search_hmicsandbox(request):

    if request.method == 'POST':
        Searched = request.POST['Searched']
        hmicsandbox = HmicSandBox.objects.filter(Developer_Email_ID__contains=Searched)
        return render(request, 'Repos/search_hmicsandbox.html', {
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