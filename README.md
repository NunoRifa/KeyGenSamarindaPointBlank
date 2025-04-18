# Samarinda Token Generator

Script Python sederhana untuk mengambil token dari halaman [https://generatetoken.my.id/samarinda/TokenBelut.php](https://generatetoken.my.id/samarinda/TokenBelut.php) berdasarkan HWID (Hardware ID).  
Token yang dihasilkan akan digunakan untuk mengaktifkan atau mendaftarkan produk tertentu yang terintegrasi dengan sistem ini.

## 🛠 Fitur

- Simulasi akses halaman utama dan form generator
- Submit HWID dan trigger tombol `Generate Token`
- Parsing hasil dari respon HTML (Swal.fire script)
- Otomatis mengekstrak token dari tag HTML di dalam JavaScript

## ⚙️ Persyaratan

- Python 3.x
- Modul:
  - `requests`
  - `urllib3`

Install dengan pip jika belum ada:
```bash
pip install requests urllib3
```

## ▶️ Cara Penggunaan
- Jalankan script `NewKeyGen.py` dari terminal:
```bash
python NewKeyGen.py
```
- Lalu masukkan HWID saat diminta:
```bash
Masukkan HWID (hex 32 karakter): AE9EEB8ACEBAC3808006F786EAC2E159
```
- Outputnya akan menampilkan token jika berhasil ditemukan:
```bash
5. Token ditemukan: SMD-OL1HRD7JB2
```

## 🧠 Catatan Teknis
- Script ini tidak menggunakan JavaScript engine seperti Selenium, karena token disisipkan dalam respon HTML melalui Swal.fire JavaScript. Script ini hanya melakukan regex parsing dari isi respon.
- Untuk memicu token muncul, field `generate_token` harus dikirim saat POST, mirip seperti klik tombol manual.

## 🚨 Disclaimer
Proyek ini hanya ditujukan untuk pembelajaran dan eksperimen.
Gunakan dengan bijak dan jangan gunakan untuk aktivitas ilegal.
