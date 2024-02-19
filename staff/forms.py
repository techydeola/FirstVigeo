from django import forms
from .models import Loan


# create a django form for the login page
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


# create a django form for the loan request page
class RequestForm(forms.Form):
    loan_amount = forms.IntegerField()