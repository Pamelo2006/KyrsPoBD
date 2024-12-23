from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField()
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CardForm(forms.Form):
    nomer = forms.CharField()
    cvcode = forms.CharField(widget=forms.PasswordInput)
