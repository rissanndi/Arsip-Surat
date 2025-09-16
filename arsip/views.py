def edit_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES, instance=surat)
        if form.is_valid():
            surat = form.save(commit=False)
            # Update file_pdf jika ada file baru
            if 'file_pdf' in request.FILES:
                surat.file_pdf = request.FILES['file_pdf']
            # Update foto jika ada file baru
            if 'foto' in request.FILES:
                surat.foto = request.FILES['foto']
            surat.save()
            messages.success(request, 'Data surat berhasil diperbarui')
            return redirect('arsip:detail_surat', pk=surat.pk)
        else:
            messages.error(request, 'Periksa kembali data yang diinputkan')
    else:
        form = SuratForm(instance=surat)
    return render(request, 'arsip/edit_surat.html', {'form': form, 'surat': surat})
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
        data = request.POST.copy()
        files = request.FILES
        
        # Create new Surat instance
        surat = Surat(
            nomor_surat=data.get('nomor_surat'),
            judul=data.get('judul'),
            kategori_id=data.get('kategori'),
            file_pdf=files.get('file_pdf')
        )
        
        # Add foto if provided
        if 'foto' in files:
            surat.foto = files['foto']
        
        try:
            surat.full_clean()
            surat.save()
            messages.success(request, 'Data berhasil disimpan')
            return redirect('arsip:index')
        except ValidationError as e:
            messages.error(request, str(e))
    else:
        form = SuratForm()
    return render(request, 'arsip/form_surat.html', {'form': form})

def detail_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    response = render(request, 'arsip/detail_surat.html', {'surat': surat})
    # Allow PDF to be displayed in iframe
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Content-Security-Policy'] = "frame-ancestors 'self'"
    return response

def hapus_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    if request.method == 'POST':
        # Delete files first
        surat.file_pdf.delete(save=False)
        if surat.foto:
            surat.foto.delete(save=False)
        # Then delete the record
        surat.delete()
        messages.success(request, 'Arsip surat berhasil dihapus')
        return redirect('arsip:index')
    return render(request, 'arsip/konfirmasi_hapus.html', {'surat': surat})

def unduh_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    if not surat.file_pdf:
        messages.error(request, 'File PDF tidak ditemukan')
        return redirect('arsip:index')
        
    try:
        response = FileResponse(surat.file_pdf.open(), content_type='application/pdf')
        
        # If download parameter is present, set as attachment
        if request.GET.get('download'):
            filename = f"surat_{surat.nomor_surat.replace('/', '_')}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
        else:
            response['Content-Disposition'] = 'inline'
            
        # Add headers for better browser compatibility
        response['Accept-Ranges'] = 'bytes'
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['Content-Security-Policy'] = "frame-ancestors 'self'"
        
        # Cache control
        response['Cache-Control'] = 'public, max-age=0'
        response['Pragma'] = 'public'
            
        return response
    except Exception as e:
        messages.error(request, f'Error saat membuka file: {str(e)}')
        return redirect('arsip:index')

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
