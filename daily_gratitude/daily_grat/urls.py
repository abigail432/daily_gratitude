from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('entry', views.dailyEntry, name='entry'),
     path('thanks/', views.thanks, name='thanks'),

]