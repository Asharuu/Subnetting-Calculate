# Pohon Subnetting Interaktif (Iza's Way) — Modul 7 Jaringan Komputer

Website interaktif pembelajaran subnetting VLSM (*Variable Length Subnet Masking*) berbasis metode **Hierarki Pohon Biner (Iza's Way)** dari dokumen praktikum:
`Modul 7 subnetting.docx`.

Fokus utama adalah **IP Kelas C (Prefix /24)** dengan kemampuan mengubah alamat IP dasar (*Custom Class C IP*).

---

## 🌟 Fitur Utama

1. **Visualisasi Pohon Subnetting Biner (Iza's Way) Interaktif:**
   * **Direct Drag & Drop Node:** Setiap elemen (lingkaran subnet, kotak percabangan, maupun blok kosong) dapat di-klik dan digeser secara bebas menggunakan kursor mouse untuk mengatur tata letak sendiri jika terasa terlalu mepet.
   * Garis cabang kurva dan label bit (`0` dan `1`) otomatis melar dan mengikuti pergerakan elemen secara dinamis.
   * Struktur pohon percabangan dari level `/24` (256 IP) hingga `/30` (4 IP) lengkap dengan label Netmask desimal.

2. **📸 Ekspor Pohon ke Gambar (PNG / JPG):**
   * Simpan diagram hierarki pohon subnetting lengkap dengan 1 klik!
   * Tersedia tombol **PNG** (resolusi tinggi 2x retina dengan latar belakang rapi) dan **JPG**.
   * Sangat praktis untuk langsung dilampirkan ke laporan praktikum / tugas Microsoft Word / presentasi.

3. **🖥️ Mode Layar Penuh (Fullscreen):**
   * Tombol **Layar Penuh** di toolbar (atau tekan tombol **F** di keyboard).
   * Memaksimalkan area kanvas ke seluruh layar monitor sehingga pohon besar (seperti tugas 10 subnet A–J) dapat dilihat dengan sangat lega dan jelas tanpa gangguan.

4. **🎛️ Pengatur Jarak Cabang (Spacing Sliders):**
   * Slider **Jarak Cabang (Lebar)** (90px s/d 280px) untuk melonggarkan cabang secara horizontal.
   * Slider **Tinggi Tingkat** (80px s/d 170px) untuk mengatur jarak vertikal antar level prefix.
   * Tombol **Pusatkan** dan **Reset Posisi Elemen** untuk mengembalikan tata letak ke kalkulasi otomatis.

5. **Kustomisasi IP Kelas C Bebas:**
   * Masukkan IP Jaringan Kelas C apapun (contoh: `192.168.15.0`, `172.16.20.0`, `192.168.1.0`, `10.0.0.0/24`, dll).
   * Seluruh hierarki pohon, tabel subnet, dan topologi otomatis terhitung dan diperbarui secara instan (*real-time*).

6. **Preset Langsung dari Modul 7:**
   * **📘 Contoh Modul (7 Jaringan):** Jaringan 1 (26 user), Jaringan 2 (25 user), Jaringan 4 (20 user), Jaringan 3 (15 user), serta 3 link router serial Jaringan 5, 6, 7 (masing-masing 2 user).
   * **📝 Tugas Mandiri Modul (10 Jaringan A – J):** Jaringan B (60 user), D (50 user), A (30 user), F (30 user), E (20 user), C (10 user), dan 4 link router G, H, I, J (2 user) pada base IP `172.16.20.0/24`. Seluruh 256 IP terisi 100% pas!

7. **Detail Biner Oktet ke-4 (Modal Inspeksi):**
   * Klik pada setiap node pohon untuk melihat pembagian 8-bit oktet ke-4.
   * Formula matematika perkalian bobot biner:
     `0×2^7 + 1×2^6 + 1×2^5 = 96` persis seperti foto tulisan tangan di modul.
   * Rincian Network ID, Netmask, Range Host Valid, Broadcast, dan sisa host cadangan.

8. **Topologi Jaringan Visual:**
   * Diagram interaktif router dan cloud jaringan yang terhubung langsung dengan alokasi IP hasil pohon.

9. **Tabel Rekapitulasi & Ekspor:**
   * Salin tabel hasil dalam format **Markdown** (untuk GitHub/Notion) atau **CSV** (untuk Excel / Word).

---

## 🚀 Cara Menjalankan

Anda dapat menjalankan website ini dengan 2 cara mudah:

### Cara 1: Buka Langsung di Browser (Tanpa Instalasi Apapun)
Cukup klik ganda (*double click*) file:
`D:\Proyek\.Website\Subnetting-Calculate\index.html`
Website akan langsung terbuka di browser Anda (Chrome, Edge, Firefox, dll).

### Cara 2: Menjalankan Local Web Server
Buka terminal / PowerShell dan jalankan:
```powershell
cd "D:\Proyek\.Website\Subnetting-Calculate"
python server.py
```
Browser akan otomatis membuka `http://localhost:5173/index.html`.
