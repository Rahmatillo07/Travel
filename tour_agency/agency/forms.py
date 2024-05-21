from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Ticket,Company,Category


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category','company','name','image','comfort','about','time','price']

        widgets = {

            'category':forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Kategoriya'
            }),

            'company':forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Kompaniya'
        }),

            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rasm tanlang',
            }),


            'comfort':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Qulaylik'
        }),



            'about':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Mahsulot haqida'
        }),

            'time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vaqt',
                'type': 'datetime-local',
            })

    }



class CompanyForm(forms.ModelForm):
    model = Company
    fields = ['name']

    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Kompaniya',
                'style': 'margin-top: 10px'
        })
    }


class CategoryForm(forms.ModelForm):
    model = Category
    fields = ['name']

    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kategoriya',
                'style': 'margin-top: 10px'
        })
    }





class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'margin-top: 5px'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'margin-top: 5px'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat the password'
    }))

    class Meta:
        model = User
        fields = ('username','password1','password2')