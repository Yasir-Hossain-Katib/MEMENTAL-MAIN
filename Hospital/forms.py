from datetime import date
from django import forms
from django.conf import settings
from django.forms import widgets
from django.utils.dates import MONTHS


# from django.forms import widgets
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class CreateAppointment(forms.Form):
    m = date.today().month
    months = {m: MONTHS[m], m+1: MONTHS[m+1]}
    appointment_date = forms.DateTimeField(
        input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(months=months, years=[date.today().year], attrs={'class': 'form-date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(
        {'class': 'form-control td-input', 'type': 'time', 'placeholder': 'time'}))
    disease_details = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control td-input', 'placeholder': "Disease Details"}))


class UpdateInfo(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control'}), required=not True)
    email = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control'}), required=not True)
    phone = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    address = forms.CharField(
        label="Address", widget=forms.TextInput({'class': 'form-control'}))
    credit_card = forms.CharField(label="Credit Card", widget=forms.TextInput(
        {'class': 'form-control'}), required=not True)
    password0 = forms.CharField(label="Password", widget=forms.PasswordInput({
        'class': 'form-control',  'placeholder': 'Current Password'}), required=not True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput({
        'class': 'form-control',   'placeholder': 'Update Password'}), required=not True)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput({
        'class': 'form-control', 'placeholder': 'Re-Enter Password'}), required=not True)


class UpdateDoctorForm(UpdateInfo):
    fees = forms.FloatField(widget=forms.NumberInput())
    qualifications = forms.CharField(widget=forms.Textarea())
    education = forms.CharField(widget=forms.Textarea())
    desc = forms.CharField(widget=forms.Textarea())
    availability = forms.BooleanField(required=not True)
    specilization = forms.CharField(
        widget=forms.TextInput({'class': 'form-control'}))


class ApproveForm(forms.Form):
    choices = [
        ('', 'Approval Needed'),
        (0, 'Denied'),
        (1, 'Approved'),
    ]
    approval = forms.ChoiceField(choices=choices)


class PrescriptionForm(forms.Form):
    prescription = forms.CharField(widget=forms.Textarea(
        {'id': 'prescribe', 'placeholder': 'Prescribe'}), required=not True)
