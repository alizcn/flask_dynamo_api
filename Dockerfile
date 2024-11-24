FROM python:3.11

# Çalışma dizini
WORKDIR /app

# Gereksinimler dosyasını kopyalayın
COPY requirements.txt /app/

# Gereksinimleri yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Flask ve werkzeug sürümlerini belirleyin
RUN pip install flask==2.3.0 werkzeug==2.3.0

# Uygulama dosyalarını kopyalayın
COPY . /app/

# Flask uygulamasını çalıştırın
CMD ["flask", "run", "--host=0.0.0.0"]
