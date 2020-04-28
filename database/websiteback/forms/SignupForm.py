from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

# class CustomSignupForm(SignupForm):
#
#     first_name = forms.CharField(max_length=30, label='First Name')
#     surname = forms.CharField(max_length=30, label='surname')
#     workplace = forms.CharField(max_length=300, label='workplace')
#     position = forms.CharField(max_length=300, label='position')
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.surname = self.cleaned_data['surname']
#         user.workplace = self.workplace['surname']
#         user.position = self.position['surname']
#         user.save()
#         return user


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    surname = forms.CharField(max_length=30, label='surname')
    workplace = forms.CharField(max_length=300, label='workplace')
    position = forms.CharField(max_length=300, label='position')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'surname',
            'workplace',
            'position'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This Email is already being used"
            )
        return email
