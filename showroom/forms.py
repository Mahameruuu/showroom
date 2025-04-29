from django import forms
from .models import Mobil

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = ['merk', 'model', 'tahun', 'harga_dasar', 'pinjaman', 'suku_bunga']
        widgets = {
            'tahun': forms.NumberInput(attrs={'min': 1900, 'max': 9999}),
            'harga_dasar': forms.NumberInput(attrs={'min': 0}),
            'pinjaman': forms.NumberInput(attrs={'min': 0}),
            'suku_bunga': forms.NumberInput(attrs={'min': 0}),
        }
