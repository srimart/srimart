from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import *
class CustomerRegistrationForm(UserCreationForm):
  password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label= 'confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
    label = {'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
    


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
  password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ))
  

class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label=_("old Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}))
  
  
  new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ),
  help_text=password_validation.password_validators_help_text_html())
  
  
  new_password2 = forms.CharField(label=_("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ))
  
  


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'zipcode', 'state', 'phoneNumber']

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, instance=instance, **kwargs)


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields ="__all__"