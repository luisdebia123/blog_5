from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
    label = {'username' : 'Nombre de Usuario',
            "first_name" : 'Nombre',
            "last_name" : 'Apellido',
            "email" : 'Correo',
            "password1" : 'Password1',
            "password2" : 'Password2',
            }