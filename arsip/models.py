from django.db import models


class KategoriSurat(models.Model):
    # id field is automatically added by Django with auto_increment
    nama = models.CharField(max_length=100, unique=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

class Surat(models.Model):
    nomor_surat = models.CharField(max_length=200, unique=True)
    judul = models.CharField(max_length=255)
    kategori = models.ForeignKey(KategoriSurat, on_delete=models.PROTECT)  # Changed to PROTECT to prevent accidental deletion
    file_pdf = models.FileField(upload_to='surat_pdf/')
    foto = models.ImageField(upload_to='surat_foto/', blank=True, null=True)  # New field for photo
    tanggal_unggah = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
