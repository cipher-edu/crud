from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

User = get_user_model()

class NewUserform(UserCreationForm):
    class Meta:
        model = User
        fields  = ("username",)
        field_classes = {'username':UsernameField}