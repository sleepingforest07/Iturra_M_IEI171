from django import forms
from django.core.exceptions import ValidationError
from APP.models import Socios_Del_Club
from datetime import date, datetime
import re

class SociosForm(forms.ModelForm):
    ESTADOS = [('vigente', 'VIGENTE'), ('suspendido', 'SUSPENDIDO'), ('retirado', 'RETIRADO')]
    TIPO_SEXO = [('hombre', 'HOMBRE'), ('mujer', 'MUJER'), ('otro', 'OTRO')]
    
    Nombre_Socio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=80,
        required=True,
        label='Nombre del Socio',
    ) 
    
    Fecha_Incorporacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Fecha incorporacion (yyyy-mm-dd)')
    Fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label='Año nacimiento (yyyy-mm-dd)')
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=20, required=True)
    Correo_Electronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True,label='Correo electronico')
    Sexo = forms.CharField(widget=forms.Select(choices=TIPO_SEXO, attrs={'class': 'form-select'}), required=True)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS, attrs={'class': 'form-select'}), required=True)
    observacion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Socios_Del_Club
        fields = ['Nombre_Socio', 'Fecha_Incorporacion', 'Fecha_nacimiento', 'Telefono', 'Correo_Electronico', 'Sexo', 'estado', 'observacion']

    def clean(self):
        cleaned_data = super().clean()
        fecha_incorporacion = cleaned_data.get('Fecha_Incorporacion')
        fecha_nacimiento = cleaned_data.get('Fecha_nacimiento')

        if fecha_incorporacion and fecha_incorporacion > date.today():
            self.add_error('Fecha_Incorporacion', "La fecha de incorporación no puede ser en el futuro")

        if fecha_nacimiento:
            if fecha_nacimiento > date.today():
                self.add_error('Fecha_nacimiento', "La fecha de nacimiento no puede ser en el futuro")
            elif (date.today() - fecha_nacimiento).days < 365 * 18:
                self.add_error('Fecha_nacimiento', "El socio debe ser mayor de edad")

        nombre_socio = cleaned_data.get('Nombre_Socio')

        if nombre_socio and len(nombre_socio) >= 80:
            raise forms.ValidationError("El nombre no puede pasar los 80 caracteres")

        # Validar que el formato de las fechas sea válido
        if fecha_incorporacion and fecha_nacimiento:
            print("prueba1")
            try:
                datetime.strptime(str(fecha_incorporacion), '%Y-%m-%d')
                datetime.strptime(str(fecha_nacimiento), '%Y-%m-%d')
            except ValueError:
                self.add_error(None, "El formato de las fechas no es válido (debe ser yyyy-mm-dd)")

        return cleaned_data