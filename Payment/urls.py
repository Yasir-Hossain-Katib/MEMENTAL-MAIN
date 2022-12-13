from django.urls import path
from . import views

urlpatterns = [
    path('success/', views.success, name='success'),
    path('booking-page/<str:pk>/', views.make_appointment, name='booking-page'),
]
