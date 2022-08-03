import imp
from pyexpat import model

from attr import field
from .models import Datas
from django import forms

class DataForms(forms.ModelForm):
    class Meta:
        model =  Datas
        fields = ['name','age','height','sex']