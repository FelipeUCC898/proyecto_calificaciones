from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Calificacion


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'tu@email.com',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = [
            'nombre_estudiante',
            'identificacion',
            'asignatura',
            'nota1',
            'nota2',
            'nota3',
        ]
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez'
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Matemáticas'
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
        }

