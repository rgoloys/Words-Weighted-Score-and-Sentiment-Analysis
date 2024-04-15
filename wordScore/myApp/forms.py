#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import KeyWord
from django.contrib.auth.models import User

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


class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='Username', required=True)
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match.")

        if old_password and not self.instance.check_password(old_password):
            raise forms.ValidationError("Incorrect old password.")