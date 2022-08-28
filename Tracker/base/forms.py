from tkinter import Image
from tkinter.tix import Select
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'}),
            'file': forms.FileInput(attrs={"class":'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'Type': forms.Select(attrs={'class':'form-control'}),
            'detail': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'})
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'income_ty': forms.Select(attrs={'class':'form-control'}),
            'income_detail': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

