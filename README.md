# Prueba Técnica – Ingeniería de Datos  
**Diego Moreno – Global MVM**

Este proyecto desarrolla una solución completa a los desafíos planteados en la prueba técnica para Ingeniería de Datos.  
La prueba se centra en:

- Generación de datos sintéticos  
- Transformación y almacenamiento  
- Procesos batch  
- Modelado SQL  
- Exposición mediante API REST  
- Contenedorización (conceptual)

---

## Estructura del repositorio

# Prueba Técnica – Ingeniería de Datos  
**Diego Moreno – Global MVM**

Este proyecto desarrolla una solución completa a los desafíos planteados en la prueba técnica para Ingeniería de Datos.  
La prueba se centra en:

- Generación de datos sintéticos  
- Transformación y almacenamiento  
- Procesos batch  
- Modelado SQL  
- Exposición mediante API REST  
- Contenedorización (conceptual)

---

## Estructura del repositorio

.
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

yaml
Copiar código

---

# DESAFÍO #1 – Generación automática de datos

El script `generate_data.py` genera datos sintéticos para:

- Departamentos  
- Puestos de trabajo  
- Empleados  

Usando librerías:

- pandas  
- numpy  
- datetime  

Se generaron IDs, nombres, rangos salariales y fechas aleatorias con reproducibilidad mediante semilla.

---

# DESAFÍO #2 – Almacenamiento en CSV y Parquet

Los datos se exportan a:

**CSV**

- departments.csv  
- jobs.csv  
- employees.csv  

**Parquet**

- departments.parquet  
- jobs.parquet  
- employees.parquet  

**Elección de formatos**

- CSV: formato simple, universal y fácil de validar manualmente.  
- Parquet: formato columnar, optimizado para analítica y Data Lakes (S3, ADLS, GCS).

---

# DESAFÍO #3 – Proceso batch hacia base de datos SQL

El script `batch_load_sqlite.py`:

- Lee los CSV generados  
- Crea la base local `hr_data.db`  
- Carga las tablas:
  - departments  
  - jobs  
  - employees  
- Crea índices para mejorar consultas  

SQLite se usa como ejemplo local equivalente a una carga batch hacia un Data Warehouse en la nube.

---

# DESAFÍO #4 – Creación de una vista SQL

Se creó la vista:

`vw_employees_extended`

Incluye:

- Nombre completo del empleado  
- Puesto  
- Departamento  
- Ubicación  
- Clasificación salarial (Low, Medium, High)

Definida en:

`create_view_employees_extended.sql`

Ejecutada mediante:

`query_view_sqlite.py`

---

# DESAFÍO #5 – API REST con FastAPI

Archivo: `api.py`

Endpoints expuestos:

| Método | Endpoint                 | Descripción                     |
|--------|---------------------------|---------------------------------|
| GET    | `/`                       | Información general             |
| GET    | `/employees`              | Listado completo de empleados   |
| GET    | `/employees/{id}`         | Consulta por ID                 |
| GET    | `/employees/high-salary`  | Empleados con salario alto      |
| GET    | `/departments`            | Lista de departamentos          |
| GET    | `/jobs`                   | Lista de puestos                |

Documentación automática:

http://127.0.0.1:8000/docs

---

# DESAFÍO #6 – Despliegue con contenedores (conceptual)

Aunque Docker no pudo ejecutarse localmente, se dejó el Dockerfile configurado:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
Construcción de imagen (entorno con Docker):

nginx
Copiar código
docker build -t mvm-hr-api .
Ejecución:

arduino
Copiar código
docker run -p 8000:8000 mvm-hr-api
Quedaría expuesta en:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

Despliegue en la nube (conceptual)
Puede desplegarse en servicios como:

Azure Container Apps

Azure App Service

AWS ECS / Fargate

Google Cloud Run

Kubernetes (AKS, EKS, GKE)

Pasos generales:

Subir la imagen a un Container Registry

Crear el servicio de contenedor

Configurar puerto 8000

Exponer endpoint público o interno

Prueba de consumo
Los endpoints fueron probados exitosamente desde Swagger y desde navegador:

GET /employees

GET /employees/{id}

GET /employees/high-salary

GET /departments

GET /jobs
