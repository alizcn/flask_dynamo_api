# Python 3.11 resmi imajını kullan
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt /app/

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Flask uygulamasını başlat
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
