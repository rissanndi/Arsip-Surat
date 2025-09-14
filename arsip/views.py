from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, JsonResponse
from django.db.models import Q
from .models import Surat, KategoriSurat
from .forms import SuratForm
from django.core.exceptions import ValidationError
from django.contrib import messages
import os

def index(request):
    surat_list = Surat.objects.order_by('-tanggal_unggah')
    return render(request, 'arsip/index.html', {'surat_list': surat_list})

def about(request):
    return render(request, 'arsip/about.html')

from django.contrib import messages

def tambah_surat(request):
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil disimpan')
            return redirect('/')
    else:
        form = SuratForm()
    return render(request, 'arsip/form_surat.html', {'form': form})

def detail_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    return render(request, 'arsip/detail_surat.html', {'surat': surat})

def hapus_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    if request.method == 'POST':
        surat.file_pdf.delete(save=False)  # Delete the file first
        surat.delete()
        messages.success(request, 'Arsip surat berhasil dihapus')
        return redirect('/')
    return render(request, 'arsip/konfirmasi_hapus.html', {'surat': surat})

def unduh_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    response = FileResponse(surat.file_pdf.open(), content_type='application/pdf')
    
    # If download parameter is present, set as attachment
    if request.GET.get('download'):
        filename = f"surat_{surat.nomor_surat.replace('/', '_')}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
    else:
        response['Content-Disposition'] = 'inline'
    
    return response

def search_surat(request):
    query = request.GET.get('q', '')
    if query:
        surat_list = Surat.objects.filter(Q(judul__icontains=query))
    else:
        surat_list = Surat.objects.all()
    return render(request, 'arsip/index.html', {'surat_list': surat_list, 'query': query})

def kategori_list(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        keterangan = request.POST.get('keterangan')
        
        try:
            kategori = KategoriSurat(nama=nama, keterangan=keterangan)
            kategori.full_clean()  # Validate the model
            kategori.save()
            messages.success(request, 'Kategori berhasil ditambahkan')
            return redirect('kategori_list')
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('kategori_list')
    
    kategori_list = KategoriSurat.objects.all()
    return render(request, 'arsip/kategori_list.html', {'kategori_list': kategori_list})

def update_kategori(request, pk):
    kategori = get_object_or_404(KategoriSurat, pk=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama')
        keterangan = request.POST.get('keterangan')
        
        try:
            kategori.nama = nama
            kategori.keterangan = keterangan
            kategori.full_clean()  # Validate the model
            kategori.save()
            messages.success(request, 'Kategori berhasil diperbarui')
        except ValidationError as e:
            messages.error(request, e.messages[0])
        
        return redirect('kategori_list')
    
    return JsonResponse({'id': kategori.id, 'nama': kategori.nama, 'keterangan': kategori.keterangan})

def delete_kategori(request, pk):
    if request.method == 'POST':
        kategori = get_object_or_404(KategoriSurat, pk=pk)
        try:
            # Check if category has related letters
            if kategori.surat_set.exists():
                raise ValidationError('Kategori ini memiliki surat terkait dan tidak dapat dihapus')
            
            kategori.delete()
            messages.success(request, 'Kategori berhasil dihapus')
        except ValidationError as e:
            messages.error(request, str(e))
    
    return redirect('kategori_list')
