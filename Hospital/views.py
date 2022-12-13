from django.shortcuts import redirect, render
from .models import *
from datetime import datetime
from .forms import *
from django.contrib import messages
from Payment.models import Appointment
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.http import HttpResponse
# Create your views here.


def index(request):
    patient = ""
    return render(request, 'index.html', {'patient': patient})


def show_doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)


def doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    context = {}
    form = CreateAppointment()

    context = {'doctor': doctor,
               'form': form}

    return render(request, 'doctor.html', context)


def show_profile(request):
    if request.user.is_authenticated:
        user = request.user
        patient = Patient.objects.filter(user=user).first()
        if patient:
            form = UpdateInfo()
            form.fields['fullname'].widget.attrs['value'] = patient.name
            form.fields['email'].widget.attrs['value'] = patient.email
            form.fields['phone'].widget.attrs['value'] = patient.phone
            form.fields['credit_card'].widget.attrs['value'] = patient.credit_info
            form.fields['address'].widget.attrs['value'] = patient.address

            if request.method == 'POST':
                form = UpdateInfo(request.POST)
                if form.is_valid():
                    patient.name = form.cleaned_data['fullname']
                    patient.email = form.cleaned_data['email']
                    patient.phone = form.cleaned_data['phone']
                    patient.address = form.cleaned_data['address']
                    patient.credit_info = form.cleaned_data['credit_card']

                    password0 = form.cleaned_data['password0']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']

                    if password0 and password0 == patient.password:
                        if password1 and password1 == password2:
                            patient.password = password1
                            request.user.set_password(password1)
                            request.user.save()

                    patient.save()

            appointments = Appointment.objects.filter(
                patient=patient)
            return render(request, 'profile.html', {'appointments': appointments, 'patient': patient, 'form': form})
        else:
            doctor = Doctor.objects.get(user=user)
            form = UpdateDoctorForm()
            approve_form = ApproveForm()
            prescription_form = PrescriptionForm()
            
            form.fields['phone'].widget.attrs['value'] = doctor.phone
            form.fields['credit_card'].widget.attrs['value'] = doctor.credit_info
            form.fields['address'].widget.attrs['value'] = doctor.address
            form.fields['fees'].widget.attrs['value'] = doctor.fees
            form.fields['qualifications'].initial = doctor.qualifications
            form.fields['desc'].initial = doctor.desc
            form.fields['education'].initial = doctor.education
            form.fields['availability'].initial = doctor.availability
            form.fields['specilization'].initial = doctor.specilization
            appointments = Appointment.objects.filter(doctor=doctor)

            approve_form.fields['approval'].initial = doctor.specilization

            if request.method == 'POST':
                form = UpdateDoctorForm(request.POST)
                approve_form = ApproveForm(request.POST)
                prescription_form = PrescriptionForm(request.POST)
                
                if form.is_valid():
                    doctor.phone = form.cleaned_data['phone']
                    doctor.address = form.cleaned_data['address']
                    doctor.credit_info = form.cleaned_data['credit_card']

                    password0 = form.cleaned_data['password0']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']

                    if password0 and password0 == doctor.password:
                        if password1 and password1 == password2:
                            doctor.password = password1
                            request.user.set_password(password1)
                            request.user.save()

                    doctor.fees = form.cleaned_data['fees']
                    doctor.qualifications = form.cleaned_data['qualifications']
                    doctor.desc = form.cleaned_data['desc']
                    doctor.education = form.cleaned_data['education']
                    doctor.availability = form.cleaned_data['availability']
                    doctor.specilization = form.cleaned_data['specilization']
                    doctor.save()

                elif approve_form.is_valid():
                    approval = approve_form.cleaned_data['approval']
                    approval = int(approval)
                    appointment_id = request.POST['appointment_id']
                    appointment_id = int(appointment_id)
                    appointment = Appointment.objects.get(id=appointment_id)
                    appointment.approval = approval
                    appointment.save()

                elif prescription_form.is_valid():
                    prescription = prescription_form.cleaned_data['prescription']
                    appointment_id = request.POST['appointment_id']
                    appointment_id = int(appointment_id)
                    appointment = Appointment.objects.get(id=appointment_id)
                    # if appointment.prescription:
                    #     messages.error(request, f'You already prescribed {appointment.patient}')
                    # else:
                    appointment.prescription = prescription
                    appointment.save()

            return render(request, 'profile_doctor.html', {'doctor': doctor, 'appointments': appointments, 'form': form, 'approve_form': approve_form, 'prescription_form': prescription_form})
    else:
        return redirect('login')


def show_emergency(request):
    cabins = Emergency_Cabin.objects.all()
    return render(request, 'emergency.html', {'cabins': cabins})


def generate_prescription(request, pk):
    appointments = Appointment.objects.get(id=pk)
    patient = appointments.patient
    doctor = appointments.doctor

    patient_name = "Name: " + patient.name
    patient_email = "Email: " + patient.email
    patient_birthdate = "Birthdate: " + str(patient.birthdate)
    patient_phone = "Phone: " + patient.phone
    patient_address = "Address: " + patient.address
    disease_details = "Disease: " + appointments.disease_details
    appointment_date = "Appointment Date: " + appointments.date.strftime("%A") + ", " + appointments.date.strftime(
        "%d")+"/" + appointments.date.strftime("%m") + "/" + appointments.date.strftime("%Y")

    pdfName = patient.name + " Prescription_" + pk + '.pdf'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+pdfName
    pdf = canvas.Canvas(response)
    pdf.setTitle(appointments.patient.get_fname)

    pdfmetrics.registerFont(
        TTFont('bangers', 'Hospital/pdf_asset/Bangers-Regular.ttf')
    )
    time = datetime.now()
    time1 = "Date: "+time.strftime("%A") + ", " + time.strftime("%d")+"/" + time.strftime("%m") + \
        "/" + time.strftime("%Y")
    time2 = "Time: "+time.strftime("%I")+":" + time.strftime("%M") + \
        ":" + time.strftime("%S") + " " + time.strftime("%p")
    pdf.drawInlineImage('Hospital/pdf_asset/mental-icon-2.jpg',
                        60, 750, width=40, height=40)
    pdf.drawInlineImage('Hospital/pdf_asset/steth.png',
                        400, 50, width=150, height=120)
    pdf.setFont('bangers', 22)
    pdf.drawString(105, 760, "Memental")
    pdf.setFont('Courier', 16)
    pdf.drawString(188, 763, "Health Care")
    pdf.setFont('Courier', 12)
    pdf.drawString(55, 730, time1)
    pdf.drawString(55, 717, time2)
    pdf.line(50, 50, 50, 800)
    pdf.line(50, 50, 550, 50)
    pdf.line(50, 800, 550, 800)
    pdf.line(550, 50, 550, 800)
    pdf.line(50, 708, 550, 708)
    pdf.line(50, 587, 550, 587)

    pdf.drawString(55, 690, 'Patient Details:')
    pdf.drawString(55, 690, 'Patient Details:')
    pdf.drawString(55, 690, 'Patient Details:')
    pdf.setFont('Courier', 12)
    pdf.drawString(380, 777, "Dr. "+doctor.name.split()[-1])
    pdf.drawString(380, 777, "Dr. "+doctor.name.split()[-1])
    pdf.drawString(380, 777, "Dr. "+doctor.name.split()[-1])
    pdf.drawString(380, 762, doctor.specilization)
    pdf.drawString(380, 747, "Phone: "+doctor.phone)
    pdf.drawString(100, 675, patient_name)
    pdf.drawString(100, 675, patient_name)
    pdf.drawString(100, 675, patient_name)
    pdf.drawString(100, 661, patient_birthdate)
    pdf.drawString(100, 648, patient_email)
    pdf.drawString(100, 635, patient_phone)
    pdf.drawString(100, 622, patient_address)
    pdf.drawString(100, 609, disease_details)
    pdf.drawString(100, 609, disease_details)
    pdf.drawString(100, 609, disease_details)
    pdf.drawString(100, 596, appointment_date)
    pdf.drawString(100, 596, appointment_date)
    pdf.drawString(100, 596, appointment_date)
    pdf.drawString(55, 570, 'Precription:')
    pdf.drawString(55, 570, 'Precription:')
    pdf.drawString(55, 570, 'Precription:')

    textobject = pdf.beginText(100, 550)
    i = 1
    for line in appointments.prescription.splitlines(False):
        textobject.textLine(str(i) + ") " + line.rstrip())
        i = i + 1
    pdf.drawText(textobject)

    pdf.save()
    i = 1

    return response
