from Hospital.models import Doctor, Patient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
# Create your views here.


def login_user(request):
    form = LoginForm()
    context = {}
    if request.user.is_authenticated:
        messages.info(request, 'You are alerady logged in.')
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                if Doctor.objects.filter(user=user).exists():
                    doctor = Doctor.objects.get(user=user)
                    if not doctor.verified:
                        messages.warning(
                            request, "Need adminstration approval to continue.")
                        return redirect('login')

                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin:index'))

                return redirect('index')
            else:
                messages.info(request, 'Email and password do not match')
                return redirect('login')

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not logged in.')
        return redirect('index')

    logout(request)
    messages.success(request, 'Thank you for using our service!')
    return render(request, 'index.html')


def create_account(request):
    form = PatientCreateForm()

    if request.method == 'POST':
        form = PatientCreateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            name = f'{fname} {lname}'

            email = form.cleaned_data['email']
            if Patient.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('login')

            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                messages.warning(request, "Passwords don't match")
                return redirect('signup')

            bdate = form.cleaned_data['bdate']
            credit_card = form.cleaned_data['credit_card']

            street_address = form.cleaned_data['street_address']
            zip_code = form.cleaned_data['zip_code']
            district = form.cleaned_data['district']

            address = f'{street_address}, {district}-{zip_code}'

            phone = form.cleaned_data['phone']
            phone_type = form.cleaned_data['phone_type']
            user = User.objects.create_user(email, email, password1)

            Patient.objects.create(user=user, name=name, email=email, password=password1,
                                   birthdate=bdate, credit_info=credit_card, phone=phone, address=address)

            messages.success(request, 'Account created')

            return redirect('login')
        else:
            messages.error(request, 'Invalid Credentials')

    context = {'form': form}
    return render(request, 'signup.html', context)


def doctor_signup(request):
    form = DoctorCreateForm()

    if request.method == 'POST':
        form = DoctorCreateForm(request.POST)

        if form.is_valid():
            print('valid form')
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            name = f'{fname} {lname}'

            email = form.cleaned_data['email']
            if Patient.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('login')

            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            bdate = form.cleaned_data['bdate']
            qualifications = form.cleaned_data['qualifications']

            credit_card = form.cleaned_data['credit_card']

            street_address = form.cleaned_data['street_address']
            zip_code = form.cleaned_data['zip_code']
            fees = form.cleaned_data['fees']
            district = form.cleaned_data['district']

            address = f'{street_address}, {district}-{zip_code}'

            phone = form.cleaned_data['phone']
            phone_type = form.cleaned_data['phone_type']
            phone = f'{phone_type}{phone}'
            education = form.cleaned_data['education']
            specilization = form.cleaned_data['specilization']
            user = User.objects.create_user(email, email, password1)
            # user.save()
            Doctor.objects.create(user=user, name=name, email=email, password=password1, birthdate=bdate, credit_info=credit_card, fees=fees,
                                  phone=phone, address=address, qualifications=qualifications, specilization=specilization, education=education)
            messages.success(request, 'Account created. Wait for approval.')

            return redirect('login')

    context = {'form': form}
    return render(request, 'doctor_signup.html', context)
