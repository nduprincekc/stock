from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about.html',views.home,name='about')
]