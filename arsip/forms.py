from django import forms
from .models import Surat, KategoriSurat
from django.core.exceptions import ValidationError

class SuratForm(forms.ModelForm):
    def clean_file_pdf(self):
        file = self.cleaned_data.get('file_pdf')
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError('File harus berupa PDF.')
            return file
        return None

    class Meta:
        model = Surat
        fields = ['nomor_surat', 'kategori', 'judul', 'file_pdf']
        labels = {
            'nomor_surat': 'Nomor Surat',
            'kategori': 'Kategori',
            'judul': 'Judul',
            'file_pdf': 'File Surat (PDF)',
        }
        widgets = {
            'nomor_surat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nomor surat'
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-control'
            }),
            'judul': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan judul surat'
            }),
            'file_pdf': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
        }