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

```
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
```

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

---

# DESAFÍO #2 – Almacenamiento en CSV y Parquet

### CSV
- departments.csv  
- jobs.csv  
- employees.csv  

### Parquet
- departments.parquet  
- jobs.parquet  
- employees.parquet  

---

# DESAFÍO #3 – Proceso batch hacia SQL

El script `batch_load_sqlite.py`:

- Lee archivos CSV  
- Crea la base `hr_data.db`  
- Carga tablas  
- Crea índices para optimizar consultas  

---

# DESAFÍO #4 – Vista SQL

Se creó:

`vw_employees_extended`

Incluye:

- Nombre completo  
- Puesto  
- Departamento  
- Ubicación  
- Clasificación salarial  

---

# DESAFÍO #5 – API REST con FastAPI

Archivo: `api.py`

### Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información general |
| GET | `/employees` | Lista completa |
| GET | `/employees/{id}` | Consulta por ID |
| GET | `/employees/high-salary` | Salarios altos |
| GET | `/departments` | Lista |
| GET | `/jobs` | Lista |

Documentación:  
http://127.0.0.1:8000/docs

---

# DESAFÍO #6 – Docker (conceptual)

### Dockerfile

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Construcción:

```
docker build -t mvm-hr-api .
```

Ejecución:

```
docker run -p 8000:8000 mvm-hr-api
```

---

# Estado de pruebas

Se verificó el funcionamiento de:

- Vista SQL  
- Carga batch  
- Endpoints REST  
- Documentación Swagger  
