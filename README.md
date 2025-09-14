# Arsip Surat

## Tujuan
Aplikasi Arsip Surat dibuat untuk memudahkan pengelolaan, pencarian, dan penyimpanan arsip surat secara digital di lingkungan instansi atau organisasi.

## Fitur
- Manajemen surat masuk dan keluar
- Upload file surat (PDF)
- Kategori surat
- Pencarian surat
- Detail surat dan unduh file
- Upload foto surat (opsional)
- Tampilan responsif dan modern

## Cara Menjalankan
1. **Clone repository**
   ```bash
   git clone https://github.com/rissanndi/Arsip-Surat.git
   cd Arsip-Surat/arsip_surat_project
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Migrasi database**
   ```bash
   python manage.py migrate
   ```
4. **Jalankan server**
   ```bash
   python manage.py runserver
   ```
5. **Akses aplikasi**
   Buka browser dan akses `http://localhost:8000/`

## Screenshot

### Halaman About
![About](screenshots/about.png)

### Form Unggah Surat
![Form Surat](screenshots/form_surat.png)

### Detail Surat
![Detail Surat](screenshots/detail_surat.png)

---

© 2025 Arsip Surat
# Arsip Surat

Aplikasi web untuk manajemen arsip surat digital menggunakan Django dan MySQL, dijalankan dengan Docker.

## Fitur
- Pencarian surat berdasarkan judul melalui search bar
- Upload dan unduh file PDF surat
- Hapus surat dengan konfirmasi modal
- Lihat detail surat
- Menu About aplikasi
- Manajemen kategori surat

## Cara Menjalankan

## Cara Menjalankan dari Terminal
1. Clone repository:
   ```bash
   git clone https://github.com/rissanndi/Arsip-Surat.git
   cd Arsip-Surat
   ```
2. Build dan jalankan aplikasi:
   ```bash
   docker-compose up --build
   ```
   Setelah perintah di atas dijalankan, buka browser dan akses:
   ```
   http://localhost:8000
   ```
   untuk melihat aplikasi Arsip Surat di web.
3. Migrasi database:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. Untuk menghentikan aplikasi:
   ```bash
   docker-compose down
   ```

## Struktur Folder
```
manage.py
arsip/
    models.py
    views.py
    admin.py
    apps.py
    tests.py
    migrations/
    templates/
arsip_surat_project/
    settings.py
    urls.py
    wsgi.py
    asgi.py
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

## Kontribusi
Silakan buat pull request atau issue jika ingin berkontribusi atau melaporkan bug.

## Lisensi
MIT
