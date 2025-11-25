Prueba Técnica – Ingeniería de Datos - Diego Moreno

Global MVM

Este proyecto desarrolla la solución completa a los desafíos planteados en la prueba técnica para Ingeniería de Datos.
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

Se desarrolló un script en Python (generate_data.py) que genera automáticamente información sintética para:

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

Formato universal y legible

Útil para validación manual

Ideal para pruebas rápidas

Parquet

Formato columnar optimizado

Alto rendimiento en analítica

Estándar en Data Lakes: Amazon S3, ADLS, GCS

Ahorro en almacenamiento


DESAFÍO #3 – Proceso batch hacia base de datos SQL

Se implementó el script batch_load_sqlite.py que:

Lee los CSV generados

Crea la base SQLite hr_data.db

Carga las tablas:

departments

jobs

employees

Crea índices básicos para mejorar consultas

SQLite se utiliza como ejemplo local, equivalente a un proceso batch hacia una base SQL o Data Warehouse en la nube.


DESAFÍO #4 – Creación de una vista SQL

Se incluyó la vista:

vw_employees_extended

Que combina empleados, puestos y departamentos con campos adicionales:

Nombre completo

Detalles del puesto

Ubicación del departamento

Clasificación del salario (Low, Medium, High)

Creada mediante:

create_view_employees_extended.sql

Ejecutada desde Python con query_view_sqlite.py


DESAFÍO #5 – API REST para exponer los datos

Se implementó una API con FastAPI (api.py) que expone:

Endpoint	Descripción
GET /	Información básica
GET /employees	Lista completa de empleados
GET /employees/{id}	Detalle por ID
GET /employees/high-salary	Empleados con salario alto
GET /departments	Lista de departamentos
GET /jobs	Lista de puestos

La API quedó disponible en local:

http://127.0.0.1:8000/docs


DESAFÍO #6 – Despliegue con contenedores (Docker) y prueba de consumo

Aunque en el entorno actual no fue posible ejecutar Docker localmente, se deja lista la configuración completa para el despliegue basado en contenedores siguiendo buenas prácticas.

1 Archivo Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

2 Construcción de la imagen

En un entorno con Docker disponible:

docker build -t mvm-hr-api .

3 Ejecución del contenedor
docker run -p 8000:8000 mvm-hr-api


La API quedaría expuesta en:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs


4 Despliegue en la nube (conceptual)

El contenedor puede desplegarse sin cambios en:

Azure Container Apps

Azure App Service

AWS ECS / Fargate

Google Cloud Run

Kubernetes (AKS, EKS, GKE)

Pasos generales:

Subir imagen a un Container Registry (ACR / ECR / GCR / Docker Hub)

Crear un servicio de contenedor

Configurar variables de entorno y puerto 8000

Exponer un endpoint público o interno

5 Prueba de consumo

La API fue probada directamente desde Swagger (/docs) y mediante navegador con los endpoints:

GET /employees

GET /employees/{id}

GET /employees/high-salary

GET /departments

GET /jobs

Los resultados confirman el correcto funcionamiento del modelo, la vista SQL y la API.