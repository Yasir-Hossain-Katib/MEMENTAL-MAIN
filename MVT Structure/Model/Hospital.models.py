from django.db import models
from django.contrib.auth.models import User as Usr
from polymorphic.models import PolymorphicModel
from django.core.validators import MinLengthValidator, MinValueValidator


# Create your models here.

class User(PolymorphicModel):
    """A class to generate a user
    ...

    Attributes
    ----------
    name: models.charfield / str
        name of the customer
    address: Location
        location of a customer
    phone: int
        phone number of a customer
    email: models.EmailField
        email of a customer
    password: model
    """
    user = models.OneToOneField(
        Usr, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50, validators=[
                                MinLengthValidator(8)])
    birthdate = models.DateField(null=True)
    phone = models.CharField(max_length=15,
                             validators=[MinLengthValidator(8)], blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name


class Patient(User):
    credit_info = models.CharField(max_length=12, validators=[MinLengthValidator(12)], blank=True, null=True)

    @property
    def get_fname(self):
        return self.name.split()[0]

    @property
    def get_lname(self):
        return self.name.split()[-1]


class Doctor(User):
    credit_info = models.CharField(max_length=12,
                                   validators=[MinLengthValidator(12)], blank=True, null=True)
    fees = models.FloatField(validators=[MinValueValidator(0)], default=0)
    qualifications = models.TextField()
    education = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=False)
    desc = models.TextField(blank=True)
    specilization = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    verified = models.BooleanField(default=False)

    @property
    def get_img(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/images/placeholder.jpg'

    @property
    def get_fees(self):
        return int(self.fees+.5)

    @property
    def new_fees(self):
        return int(self.fees*1.5+.5)

    def address(self):
        return str(self.address)

    def spec(self):
        return str(self.specilization)

    def phone(self):
        return str(self.phone)


# class UserMessage(models.Model):
#     users = models.ForeignKey(
#         'Patient', on_delete=models.SET_NULL, null=True)
#     doctors = models.ForeignKey(
#         'Doctor', on_delete=models.SET_NULL, null=True)
#     query = models.TextField(default=' ', null=True)
#     reply = models.TextField(default=' ', null=True)
#     date = models.DateTimeField(default=timezone.now)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __str__(self):
#         return self.user.name

class Emergency_Cabin(models.Model):
    hospital_name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=255, null=True)
    choices = [
        (0, 'Not Available'),
        (1, 'Available'),
    ]
    availability = models.IntegerField(choices=choices, default=0)
    fees = models.FloatField(validators=[MinValueValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.hospital_name)
