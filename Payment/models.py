from django.db import models
from django.utils import timezone


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(
        'Hospital.Patient', verbose_name='patient', related_name='appointments', on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(
        'Hospital.Doctor', verbose_name='doctor', related_name='appointments', on_delete=models.SET_NULL, null=True)
    prescription = models.TextField(blank=True, null=True)
    disease_details = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
    choices = [
        (-1, 'Waiting doctors approval'),
        (0, 'Denied'),
        (1, 'Approved'),
    ]
    approval = models.IntegerField(choices=choices, default=-1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    def get_doctor_name(self):
        return str(self.doctor.name)

    def get_doctor_email(self):
        return str(self.doctor.email)

    def get_doctor_contact(self):
        return str(self.doctor.phone)

    def get_doctor_fees(self):
        return str(self.doctor.fees)

    def get_patient_name(self):
        return str(self.patient.name)

    def get_patient_email(self):
        return str(self.patient.email)

    def get_patient_contact(self):
        return str(self.patient.phone)

    @property
    def needs_approval(self):
        return self.approval == -1

    @property
    def is_approved(self):
        return self.approval == 1

    @property
    def choice(self):
        return self.choices[self.approval+1][1]
