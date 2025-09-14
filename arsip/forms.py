from django import forms
from .models import Surat

class SuratForm(forms.ModelForm):
    class Meta:
        model = Surat
        fields = ['nomor_surat', 'kategori', 'judul', 'file_pdf']
        widgets = {
            'nomor_surat': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'file_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }