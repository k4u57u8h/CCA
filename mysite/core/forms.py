from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label="Password:")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password:")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'password1': None,
            'password2': None, }
