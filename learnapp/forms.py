from django import forms
from django.contrib.auth.models import User
from learnapp.models import Userprofile
from django_recaptcha.fields import ReCaptchaField
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['phone','address','city','state','zipcode','image']
    captcha = ReCaptchaField()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
       

