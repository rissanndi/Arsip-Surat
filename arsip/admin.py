from django.contrib import admin
from .models import KategoriSurat, Surat

@admin.register(KategoriSurat)
class KategoriSuratAdmin(admin.ModelAdmin):
    list_display = ('nama', 'keterangan')
    search_fields = ('nama', 'keterangan')

@admin.register(Surat)
class SuratAdmin(admin.ModelAdmin):
    list_display = ('nomor_surat', 'judul', 'kategori', 'tanggal_unggah')
    list_filter = ('kategori', 'tanggal_unggah')
    search_fields = ('nomor_surat', 'judul')
