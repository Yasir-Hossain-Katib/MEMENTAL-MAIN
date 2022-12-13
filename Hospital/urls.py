from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.show_doctors, name='doctors'),
    path('doctor/<str:pk>/', views.doctor, name='doctor'),
    path('generate_prescription/<str:pk>/',
         views.generate_prescription, name='generate_prescription'),
    path('profile/', views.show_profile, name='profile'),
    path('emergency/', views.show_emergency, name='emergency'),
]
