from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
        widgets = {
           'username': forms.TextInput(attrs={"class": "form-control"}),
           'email': forms.EmailInput(attrs={"class": "form-control"}),
           'password': forms.PasswordInput(attrs={"class": "form-control"}),
        }
        # exclude = ('password2',)

