from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.db.models import Q
from .models import Surat
from .forms import SuratForm
import os

def index(request):
    surat_list = Surat.objects.order_by('-tanggal_unggah')
    return render(request, 'arsip/index.html', {'surat_list': surat_list})

def about(request):
    return render(request, 'arsip/about.html')

def tambah_surat(request):
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
        return redirect('/')
    return render(request, 'arsip/konfirmasi_hapus.html', {'surat': surat})

def unduh_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    response = FileResponse(surat.file_pdf.open(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(surat.file_pdf.name)}"'
    return response

def search_surat(request):
    query = request.GET.get('q', '')
    if query:
        surat_list = Surat.objects.filter(Q(judul__icontains=query))
    else:
        surat_list = Surat.objects.all()
    return render(request, 'arsip/index.html', {'surat_list': surat_list, 'query': query})
