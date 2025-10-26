from django.urls import path
from . import views

app_name = 'dtJourney'

urlpatterns = [
    path('', views.index, name='index'),            # homepage
    path('about/', views.about_me, name='about_me') # about page
]
