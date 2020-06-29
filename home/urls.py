from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleExample

urlpatterns = [
    path('', views.home, name='home'),
    path('world_confirmed/', views.world_confirmed, name='world_confirmed'),
    path('world_deaths/', views.world_deaths, name='world_deaths'),
    path('world_recovered/', views.world_recovered, name='world_recovered'),
    path('world_active/', views.world_active, name='world_active'),
    
    path('world_perkembangan_persebaran/', views.world_perkembangan_persebaran, name='world_perkembangan_persebaran'),


    path('us_confirmed/', views.us_confirmed, name='us_confirmed'),
    path('us_deaths/', views.us_deaths, name='us_deaths'),

    path('brazil_confirmed/', views.brazil_confirmed, name='brazil_confirmed'),
    path('brazil_deaths/', views.brazil_deaths, name='brazil_deaths'),

    path('china_confirmed/', views.china_confirmed, name='china_confirmed'),
    path('china_deaths/', views.china_deaths, name='china_deaths'),
    path('china_recovered/', views.china_recovered, name='china_recovered'),
    path('china_active/', views.china_active, name='china_active'),

]