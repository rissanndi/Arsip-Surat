from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'arsip'  # Menambahkan namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('surat/tambah/', views.tambah_surat, name='tambah_surat'),
    path('surat/detail/<int:pk>/', views.detail_surat, name='detail_surat'),
    path('surat/hapus/<int:pk>/', views.hapus_surat, name='hapus_surat'),
    path('surat/unduh/<int:pk>/', views.unduh_surat, name='unduh_surat'),
    path('surat/search/', views.search_surat, name='search_surat'),
    path('surat/edit/<int:pk>/', views.edit_surat, name='edit_surat'),
    # Category management URLs
    path('kategori/', views.kategori_list, name='kategori_list'),
    path('kategori/update/<int:pk>/', views.update_kategori, name='update_kategori'),
    path('kategori/delete/<int:pk>/', views.delete_kategori, name='delete_kategori'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)