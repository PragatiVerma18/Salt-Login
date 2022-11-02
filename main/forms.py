from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50,
                             widget=forms.EmailInput, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.clean_email()
        if commit:
            user.save()
        return user
