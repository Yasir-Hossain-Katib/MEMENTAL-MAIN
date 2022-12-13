from django import forms
from django.conf import settings
from datetime import date

from django.forms import widgets
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class create_booking(forms.Form):
    # Your Details
    fname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
                            'name': "firstname_booking", 'id': "firstname_booking", 'class': "form-control", 'placeholder': "{{patient.get_fname}}"}), required=not True)
    lname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                            'name': "lastname_booking", 'id': "lastname_booking", 'class': "form-control", 'placeholder': "{{patient.get_lname}}"}), required=not True)

    email1 = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
        'name': "email_booking", 'class': "form-control", 'id': "email_booking", 'placeholder': "{{patient.email}}"}), required=not True)
    email2 = forms.EmailField(label="Confirm email", widget=forms.TextInput(attrs={
        'name': "email_booking_2", 'class': "form-control", 'id': "email_booking_2", 'placeholder': "{{patient.email}}"}), required=not True)
    phone = forms.CharField(label="Telephone", widget=forms.TextInput(attrs={
                            'name': "telephone_booking", 'class': "form-control", 'id': "telephone_booking", 'placeholder': "{{patient.phone}}"}), required=not True)

    # Payment Information
    name_on_card = forms.CharField(label="Name on card", widget=forms.TextInput(
        {'class': "form-control", 'id': "name_card_booking", 'name': "name_card_booking", 'placeholder': "{{patient.name}}"}))
    card_no = forms.CharField(label="Card number", widget=forms.TextInput(
        {'class': "form-control", 'id': "card_number", 'name': "card_number", 'placeholder': "{{patient.credit_info}}"}))
    exp_month = forms.CharField(widget=forms.TextInput(
        {'class': "form-control", 'id': "expire_month", 'name': "expire_month", 'placeholder': "MM"}))
    exp_year = forms.CharField(widget=forms.TextInput(
        {'class': "form-control", 'id': "expire_year", 'name': "expire_year", 'placeholder': "Year"}))
