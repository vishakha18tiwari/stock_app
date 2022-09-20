from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class signup_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','email','role']
      
class login_form(forms.Form):
    username= forms.CharField(max_length=200, required=True)
    password= forms.CharField( max_length=200, required=True)

