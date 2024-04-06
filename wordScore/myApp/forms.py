#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import KeyWord


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FileUploadForm(forms.Form):
        file = forms.FileField()



class KeyWordForm(forms.ModelForm):
    class Meta:
        model = KeyWord
        fields = ['keywords', 'score', 'color_code']
        widgets = {
            'color_code': forms.TextInput(attrs={'value': '#000000'})  # Provide default color code
        }



class DocumentForm(forms.Form):
    document = forms.FileField(label='')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())