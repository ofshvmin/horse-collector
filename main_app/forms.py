from django import forms
from django.forms import ModelForm
from .models import FarrierAppt
# from django.forms.fields import DateField


class FarrierApptForm(ModelForm):
  class Meta:
    model = FarrierAppt
    fields = ['date', 'service']
    
  date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))