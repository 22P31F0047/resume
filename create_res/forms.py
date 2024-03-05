from django import forms
from .models import register
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=register
        fields=['firstname','middlename','lastname','dob','emailaddress','gender','user_name','password','confirmpassword']
