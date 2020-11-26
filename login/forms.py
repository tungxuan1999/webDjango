from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'class': "form-control form-control-user",'placeholder':"Username"}))
    # firstname = forms.CharField(label='First Name')
    # lastname = forms.CharField(label='Last Name')
    email = forms.CharField(label='',widget=forms.EmailInput(attrs={'class': "form-control form-control-user",'placeholder':"Email"}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': "form-control form-control-user",'placeholder':"Password"}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': "form-control form-control-user",'placeholder':"Repeat Password"}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError('Password is fail')
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError("Email exist")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Username has special characters')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username exist")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'class': "form-control form-control-user",'placeholder':"Username"}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': "form-control form-control-user",'placeholder':"Password"}))
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.search(r'^\w+$',username):
    #         raise forms.ValidationError('Username has special characters')
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         raise forms.ValidationError("Username not exist")
    #     return username
    # def save(self):
    #     user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
    #     if user is not None:
    #         return user
    #     else:
    #         return None