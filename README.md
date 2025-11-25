Prueba Técnica – Ingeniería de Datos
Diego Moreno – Global MVM

Este proyecto desarrolla la solución a los desafíos planteados en la prueba técnica para Ingeniería de Datos.
La prueba se centra en:

Generación de datos sintéticos

Transformación y almacenamiento

Procesos batch

Modelado SQL

Exposición mediante API REST

Contenedorización (conceptual)

Estructura del repositorio
├── generate_data.py
├── batch_load_sqlite.py
├── query_view_sqlite.py
├── create_view_sqlite.sql
├── api.py
├── requirements.txt
├── Dockerfile
│
├── departments.csv
├── jobs.csv
├── employees.csv
├── hr_data.db
│
├── departments.parquet
├── jobs.parquet
├── employees.parquet
└── README.md

DESAFÍO #1 – Generación automática de datos

Se desarrolló un script en Python (generate_data.py) que genera información sintética para:

Departamentos

Puestos de trabajo

Empleados

Usando:

pandas

numpy

datetime

La generación incluye IDs, nombres, rangos salariales y fechas aleatorias con reproducibilidad por semilla.

DESAFÍO #2 – Almacenamiento en CSV y Parquet

Los datos generados se exportan a:

departments.csv

jobs.csv

employees.csv

departments.parquet

jobs.parquet

employees.parquet

Elección de formatos

CSV

Legible y universal

Fácil de validar

Útil para pruebas rápidas

Parquet

Formato columnar optimizado

Alto rendimiento en analítica

Eficiente en almacenamiento

Estándar en Data Lakes

DESAFÍO #3 – Proceso batch hacia base de datos SQL

Script: batch_load_sqlite.py

Acciones:

Lee los CSV generados

Crea la base SQLite hr_data.db

Carga las tablas: departments, jobs, employees

Crea índices básicos

SQLite se utiliza como un equivalente local a una base SQL o Data Warehouse.

DESAFÍO #4 – Creación de una vista SQL

Se creó la vista:

vw_employees_extended

Incluye:

Nombre completo

Detalles del puesto

Ubicación del departamento

Clasificación salarial: Low, Medium, High

Archivos asociados:

create_view_employees_extended.sql

query_view_sqlite.py

DESAFÍO #5 – API REST

Se implementó una API con FastAPI (api.py) con los siguientes endpoints:

Endpoint	Descripción
GET /	Información básica
GET /employees	Lista de empleados
GET /employees/{id}	Consulta por ID
GET /employees/high-salary	Empleados con salario alto
GET /departments	Lista de departamentos
GET /jobs	Lista de puestos

Documentación automática disponible en:

http://127.0.0.1:8000/docs

DESAFÍO #6 – Contenedorización y prueba de consumo

Aunque no fue posible ejecutar Docker localmente, se deja lista la configuración completa.

1. Archivo Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

2. Construcción de la imagen
docker build -t mvm-hr-api .

3. Ejecución del contenedor
docker run -p 8000:8000 mvm-hr-api


Acceso a la API:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

4. Despliegue en la nube (conceptual)

El contenedor puede desplegarse en:

Azure Container Apps

Azure App Service

AWS ECS / Fargate

Google Cloud Run

Kubernetes

Pasos:

Subir imagen a un Container Registry

Crear un servicio de contenedor

Configurar variables de entorno y puerto 8000

Exponer el endpoint

5. Pruebas de consumo

Probado correctamente con:

GET /employees

GET /employees/{id}

GET /employees/high-salary

GET /departments

GET /jobs

Los resultados confirman el funcionamiento del modelo, la vista SQL y la API.
