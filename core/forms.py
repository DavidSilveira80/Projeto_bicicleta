from django import forms
from .models import *


class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = '__all__'