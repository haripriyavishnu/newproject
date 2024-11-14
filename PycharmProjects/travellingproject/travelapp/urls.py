
from django.contrib import admin
from django.urls import path
from travelapp import views


urlpatterns=[
    path('',views.login),
    path('login_post',views.login_post),
    path('add_user',views.add_user),
    path('add_user_POST',views.add_user_POST),
    path('logout',views.logout),
    path('adminpage',views.adminpage),
    path('userpage',views.userpage),



]