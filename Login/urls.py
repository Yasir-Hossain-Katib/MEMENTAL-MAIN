from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.create_account, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),
]
