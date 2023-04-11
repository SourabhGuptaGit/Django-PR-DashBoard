from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home page'),
    # path('test/', views.test, name='test page'),
    path('hmicsandbox/', views.hmicsandbox, name='hmicsandbox page'),
    path('fcc/', views.fcc, name='fcc page'),
    path('rcc/', views.rcc, name='rcc page'),
    path('rtosapps/', views.rtosapps, name='rtosapps page'),
    path('searched/', views.searched, name='all-searched'),
    path('hmicsandbox/date-search/', views.searched_btw_dates, name='hmicsandbox date search'),
    path('fcc/date-search/', views.searched_btw_dates, name='fcc date search'),
    path('rcc/date-search/', views.searched_btw_dates, name='rcc date search'),
    path('rtosapps/date-search/', views.searched_btw_dates, name='rtosapps date search'),
    path('repo-dates csv request/', views.csv_search_btw_dates, name='csv request'),
    path('hmicsandbox/csv request/', views.csv_repos, name='csv hmicsandbox'),
    path('fcc/csv request/', views.csv_repos, name='csv fcc'),
    path('rcc/csv request/', views.csv_repos, name='csv rcc'),
    path('rtosapps/csv request/', views.csv_repos, name='csv rtosapps'),

]
