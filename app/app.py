from flask import Flask, render_template_string
import pandas as pd
import io

app = Flask(__name__)

# Template HTML sederhana untuk menampilkan hasil
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analisa Data Sederhana</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
        h1 { color: #0056b3; }
        .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hasil Analisa Data Sederhana</h1>
        <h2>Data Mentah:</h2>
        {{ data_html | safe }} {# Menampilkan DataFrame sebagai tabel HTML #}

        <h2>Statistik Dasar:</h2>
        <ul>
            <li>Jumlah Baris Data: {{ total_rows }}</li>
            <li>Rata-rata Usia: {{ avg_usia | round(2) }}</li>
            <li>Rata-rata Nilai: {{ avg_nilai | round(2) }}</li>
        </ul>

        <p>Aplikasi ini dibuat dengan Flask dan Docker.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        # Membaca data dari file CSV
        # Path relatif di dalam container, karena data.csv akan disalin ke /app
        df = pd.read_csv('data.csv')

        # Analisa Sederhana
        total_rows = len(df)
        avg_usia = df['Usia'].mean()
        avg_nilai = df['Nilai'].mean()

        # Konversi DataFrame ke HTML untuk ditampilkan
        data_html = df.to_html(index=False)

        return render_template_string(HTML_TEMPLATE,
                                      data_html=data_html,
                                      total_rows=total_rows,
                                      avg_usia=avg_usia,
                                      avg_nilai=avg_nilai)
    except Exception as e:
        return f"Terjadi kesalahan saat membaca atau menganalisis data: {e}", 500

if __name__ == '__main__':
    # Jalankan aplikasi Flask pada semua interface publik di port 80
    app.run(host='0.0.0.0', port=80)