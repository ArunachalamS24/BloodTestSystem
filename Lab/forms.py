from django import forms
from .models import *

class LabRegisterform(forms.ModelForm):
    class Meta:
        model=LabRegister
        fields = '__all__'


class appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class Testform(forms.ModelForm):
    class Meta:
        model = Test_category
        fields = '__all__'

