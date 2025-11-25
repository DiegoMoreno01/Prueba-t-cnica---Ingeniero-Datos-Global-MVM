# Imagen base ligera
FROM python:3.12-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar TODO el código del proyecto
COPY . .

# Exponer el puerto donde correrá la API
EXPOSE 8000

# Comando de arranque de la API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
