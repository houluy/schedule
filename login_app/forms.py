from django import forms

class User_form(forms.Form):
    username = forms.CharField(max_length=16)
    email = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
    birth = forms.DateTimeField()

