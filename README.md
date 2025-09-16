# Arsip Surat

Aplikasi web untuk manajemen arsip surat digital di lingkungan instansi/organisasi. Dibangun dengan Django, Bootstrap, dan MySQL. Mendukung upload file PDF, pencarian, kategori, dan tampilan responsif.

---

## Tujuan
Menyediakan solusi digital untuk mengelola, mencari, dan menyimpan arsip surat secara efisien dan terstruktur.

## Fitur Utama
- Manajemen surat masuk & keluar
- Upload & unduh file PDF surat
- Kategori surat
- Pencarian surat (search bar)
- Detail surat & preview file
- Upload foto surat (opsional)
- Hapus surat dengan konfirmasi modal
- Menu About aplikasi
- Tampilan responsif & modern

---

## Cara Menjalankan

### 1. Jalankan Secara Manual (Tanpa Docker)
1. Clone repository:
   ```bash
   git clone https://github.com/rissanndi/Arsip-Surat.git
   cd Arsip-Surat/arsip_surat_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Migrasi database:
   ```bash
   python manage.py migrate
   ```
4. Jalankan server:
   ```bash
   python manage.py runserver
   ```
5. Buka browser dan akses:
   ```
   http://localhost:8000/
   ```

### 2. Jalankan dengan Docker
1. Clone repository:
   ```bash
   git clone https://github.com/rissanndi/Arsip-Surat.git
   cd Arsip-Surat
   ```
2. Build & jalankan aplikasi:
   ```bash
   docker-compose up --build
   ```
3. Migrasi database (di container):
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. Untuk menghentikan aplikasi:
   ```bash
   docker-compose down
   ```

---

## Screenshot

### Halaman About
![About](screenshots/about.png)

### Form Unggah Surat
![Form Surat](screenshots/form_surat.png)

### Detail Surat
![Detail Surat](screenshots/detail_surat.png)

---

## Struktur Folder
```
arsip_surat_project/
    settings.py
    urls.py
    wsgi.py
    asgi.py
arsip/
    models.py
    views.py
    admin.py
    apps.py
    tests.py
    migrations/
    templates/
manage.py
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

## Kontribusi
Silakan buat pull request atau issue jika ingin berkontribusi atau melaporkan bug.

## Lisensi
MIT
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
