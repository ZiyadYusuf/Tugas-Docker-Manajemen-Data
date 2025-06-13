# Menggunakan image dasar Python. Pilih versi yang stabil.
FROM python:3.9-slim-buster

# Mengatur direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke direktori kerja
COPY requirements.txt .

# Menginstal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file aplikasi ke direktori kerja container
COPY . .

# Mengekspos port 80 agar dapat diakses dari luar container
EXPOSE 80

# Mendefinisikan perintah yang akan dijalankan saat container dimulai
CMD ["python", "app.py"]