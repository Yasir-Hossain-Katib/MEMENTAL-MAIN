from Hospital.views import doctor
from .models import Appointment
from Hospital.forms import CreateAppointment
from Hospital.models import Doctor, Patient
from datetime import datetime
from dateutil import parser
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.formats import localize
from django.utils import timezone
from .forms import *
# Create your views here.

# @login_required


def payment(request):
    return render(request, 'payment.html')


def make_appointment(request, pk):
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CreateAppointment(request.POST)
        if form.is_valid():
            doctor = Doctor.objects.get(id=pk)
            patient = Patient.objects.get(email=request.user.email)
            context.update({'prev_form': form.cleaned_data,
                           'doctor': doctor, 'patient': patient})

    return render(request, 'boooking_page.html', context)


def success(request):
    context = {}
    if request.method == 'POST' and request.user.is_authenticated:
        POST = request.POST
        doctor_id = POST['doctor_id']
        appointment_date = POST['appointment_date']
        disease_details = POST['disease_details']
        appointment_date = appointment_date.replace('midnight', '')
        appointment_time = POST['appointment_time']
        date = f'{appointment_date}{appointment_time}'
        date = parser.parse(date)

        patient = Patient.objects.get(email=request.user.email)
        doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(
            patient=patient, doctor=doctor, disease_details=disease_details, date=date)

        context = {'doctor_id': doctor_id,
                   'appointment_time': appointment_time, 'user_email': request.user.username}
    return render(request, 'success.html', context)
