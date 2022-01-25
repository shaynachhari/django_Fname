from django.contrib import admin
from django.urls import path
from .import views

app_name = 'hy'
urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.stu, name='student'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('some/', views.some, name='some'),
    path('degin', views.degin, name='degin'),
    path('login/', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('singup', views.singup, name='singup'),
    path('createuser', views.createuser, name='createuser')

]
