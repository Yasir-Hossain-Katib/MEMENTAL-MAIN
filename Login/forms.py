from django import forms
from django.conf import settings
from datetime import date

from django.forms import widgets
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class PatientCreateForm(forms.Form):
    fname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
                            'name': "first_name", 'id': "first_name", 'class': "input-text", 'placeholder': "First Name"}))
    lname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                            'name': "last_name", 'id': "last_name", 'class': "input-text", 'placeholder': "Last Name"}))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
                             'name': "company", 'class': "company", 'id': "company", 'placeholder': "Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Re-Enter Password'}))

    bdate = forms.DateField(
        label="Birthdate", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(attrs={'class': 'form-date'}, years=[*range(date.today().year-100, date.today().year)][::-1]))
    credit_card = forms.CharField(label="Credit Card", widget=forms.TextInput(
        {'placeholder': "Credit card"}), required=not True)
    street_address = forms.CharField(widget=forms.TextInput(
        {'name': "street", 'class': "street", 'id': "street", 'placeholder': "House + Street Number"}))
    zip_code = forms.IntegerField(widget=forms.TextInput(
        {'name': "zip", 'class': "zip", 'id': "zip", 'placeholder': "Zip Code"}))
    district = forms.ChoiceField(choices=[('', 'Division'),
                                          ('Dhaka', 'Dhaka'),
                                          ('Rajshahi', 'Rajshahi'),
                                          ('Chittagong', 'Chittagong'),
                                          ('Barishal', 'Barishal'),
                                          ('Sylhet', 'Sylhet'),
                                          ('Khulna', 'Khulna'),
                                          ('Rangpur', 'Rangpur'),
                                          ('Mymensingh', 'Mymensingh'),
                                          ])
    phone_type = forms.ChoiceField(choices=[('+88', 'Phone'),
                                            ('02', 'Telephone')
                                            ])
    phone = forms.CharField(label="Phone no", widget=forms.TextInput(attrs={
                            'name': "phone", 'class': 'phone', 'id': "phone", 'placeholder': "Phone Number"}))


class DoctorCreateForm(forms.Form):
    fname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
                            'name': "first_name", 'id': "first_name", 'class': "input-text", 'placeholder': "First Name"}))
    lname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                            'name': "last_name", 'id': "last_name", 'class': "input-text", 'placeholder': "Last Name"}))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
                             'name': "company", 'class': "company", 'id': "company", 'placeholder': "Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Re-Enter Password'}))

    bdate = forms.DateField(
        label="Birthdate", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(attrs={'class': 'form-date'}, years=[*range(date.today().year-100, date.today().year-20)][::-1]))

    qualifications = forms.CharField(label='Qualifications', widget=forms.Textarea(
        {'name': "qualifications", 'class': "qualifications", 'id': "qualifications", 'placeholder': "List of Qualifications"}))
    specilization = forms.CharField(
        widget=forms.TextInput({'placeholder': "Specialization"}))
    credit_card = forms.CharField(label="Credit Card", widget=forms.TextInput(
        {'name': "additional", 'class': "additional", 'id': "additional", 'placeholder': "Credit card"}), required=not True)
    street_address = forms.CharField(widget=forms.TextInput(
        {'name': "street", 'class': "street", 'id': "street", 'placeholder': "House + Street Number"}))
    zip_code = forms.IntegerField(widget=forms.TextInput(
        {'name': "zip", 'class': "zip", 'id': "zip", 'placeholder': "Zip Code"}))
    fees = forms.FloatField(widget=forms.TextInput(
        attrs={'type': "number", 'placeholder': "Fees"}))
    district = forms.ChoiceField(choices=[('', 'Division'),
                                          ('Dhaka', 'Dhaka'),
                                          ('Rajshahi', 'Rajshahi'),
                                          ('Chittagong', 'Chittagong'),
                                          ('Barishal', 'Barishal'),
                                          ('Sylhet', 'Sylhet'),
                                          ('Khulna', 'Khulna'),
                                          ('Rangpur', 'Rangpur'),
                                          ('Mymensingh', 'Mymensingh'),
                                          ])
    phone_type = forms.ChoiceField(choices=[('+88', 'Phone'),
                                            ('02', 'Telephone')
                                            ])
    phone = forms.CharField(label="Phone no", widget=forms.TextInput(attrs={
                            'name': "phone", 'class': 'phone', 'id': "phone", 'placeholder': "Phone Number"}))

    education = forms.CharField(label='Education', widget=forms.Textarea(
        {'name': "education", 'class': "education", 'id': "education", 'placeholder': "List of Med-schools"}))


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': 'example@email.com'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Password'}))
