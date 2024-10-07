from django import forms 
from .models import Cantores

class CantorForm(forms.ModelForm):
    class Meta:
        model = Cantores
        fields = ['nome', 'estilo']