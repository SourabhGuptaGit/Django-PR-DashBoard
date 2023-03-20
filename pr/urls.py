from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home page'),
    path('hmicsandbox/', views.hmicsandbox, name='hmicsandbox page'),
    path('fcc/', views.fcc, name='fcc page'),
    path('rcc/', views.rcc, name='rcc page'),
    path('rtosapps/', views.rtosapps, name='rtosapps page'),
    path('searched/', views.searched, name='all-searched'),
    # path('search hmicsandbox', views.search_hmicsandbox, name='search-hmicsandbox'),
    # path('search fcc', views.search_FCC, name='search-fcc'),
    # path('search rcc', views.search_RCC, name='search-rcc'),
    # path('search rtosapps', views.search_RtosApps, name='search-rtosapps'),
]
