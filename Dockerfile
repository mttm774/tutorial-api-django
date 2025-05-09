# Usa una imagen base ligera con Python
FROM python:3.11-slim

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crea y usa un directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copia los archivos y requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto 80, como espera Azure App Service
EXPOSE 80

# Comando de inicio con Gunicorn
CMD ["gunicorn", "GestionVehiculos.wsgi:application", "--bind", "0.0.0.0:80"]
