from django.db import models


class KategoriSurat(models.Model):
    nama_kategori = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama_kategori

class Surat(models.Model):
    nomor_surat = models.CharField(max_length=200, unique=True)
    judul = models.CharField(max_length=255)
    kategori = models.ForeignKey(KategoriSurat, on_delete=models.CASCADE)
    file_pdf = models.FileField(upload_to='surat_pdf/')
    tanggal_unggah = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
