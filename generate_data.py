import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Fijamos semilla para reproducibilidad
np.random.seed(42)


# 1. Datos de Departamentos

departments_data = {
    "department_id": [10, 20, 30, 40, 50],
    "department_name": [
        "Engineering",
        "Data Science",
        "Human Resources",
        "Sales",
        "Finance"
    ],
    "location": [
        "Bogota",
        "Medellin",
        "Bogota",
        "Cali",
        "Bogota"
    ]
}

departments_df = pd.DataFrame(departments_data)


# 2. Datos de Puestos

jobs_data = {
    "job_id": [100, 101, 102, 103, 104, 105, 106, 107],
    "job_title": [
        "Data Engineer Jr",
        "Data Engineer Sr",
        "Data Analyst",
        "HR Specialist",
        "Sales Representative",
        "Sales Manager",
        "Software Engineer",
        "Finance Analyst"
    ],
    # Relacionamos cada puesto con un departamento
    "department_id": [20, 20, 20, 30, 40, 40, 10, 50],
    "salary_min": [3500, 6000, 3000, 2800, 2500, 5000, 4000, 3200],
    "salary_max": [5500, 9000, 5000, 4500, 4500, 8000, 7500, 6000]
}

jobs_df = pd.DataFrame(jobs_data)


# 3. Datos Empleados


num_employees = 200  # cuántos empleados quieres simular

first_names = [
    "Diego", "Laura", "Juan", "Ana", "Carlos", "Maria", "Luis",
    "Camila", "Jorge", "Valentina", "Andres", "Diana"
]
last_names = [
    "Gomez", "Rodriguez", "Perez", "Lopez", "Martinez", "Garcia",
    "Fernandez", "Ramirez", "Torres", "Moreno", "Vargas", "Castro"
]

def random_date(start_date: datetime, end_date: datetime) -> datetime:
    """Devuelve una fecha aleatoria entre start_date y end_date."""
    delta_days = (end_date - start_date).days
    random_days = np.random.randint(0, delta_days + 1)
    return start_date + timedelta(days=random_days)

start_hire = datetime(2018, 1, 1)
end_hire = datetime(2024, 12, 31)

employee_rows = []

for emp_id in range(1, num_employees + 1):
    # Escogemos un puesto de trabajo al azar
    job_row = jobs_df.sample(1).iloc[0]

    # Nombre y apellido aleatorios
    first = np.random.choice(first_names)
    last = np.random.choice(last_names)

    email = f"{first.lower()}.{last.lower()}{emp_id}@example.com"

    # Fecha de contratación aleatoria en los últimos años
    hire_date = random_date(start_hire, end_hire)

    # Salario aleatorio dentro del rango definido para el puesto
    salary = np.random.randint(job_row["salary_min"], job_row["salary_max"] + 1)

    employee_rows.append(
        {
            "employee_id": emp_id,
            "first_name": first,
            "last_name": last,
            "email": email,
            "hire_date": hire_date,
            "department_id": job_row["department_id"],  # consistente con el puesto
            "job_id": job_row["job_id"],
            "salary": salary
        }
    )

employees_df = pd.DataFrame(employee_rows)


# 4. Vista rápida


if __name__ == "__main__":
    print("=== Departments ===")
    print(departments_df.head(), "\n")

    print("=== Jobs ===")
    print(jobs_df.head(), "\n")

    print("=== Employees ===")
    print(employees_df.head(), "\n")

    print(f"Total employees generated: {len(employees_df)}")



# 5. Guardar en CSV

departments_df.to_csv("departments.csv", index=False)
jobs_df.to_csv("jobs.csv", index=False)
employees_df.to_csv("employees.csv", index=False)

print("Archivos CSV generados exitosamente.")



# 6. Guardar en Parquet

departments_df.to_parquet("departments.parquet", index=False)
jobs_df.to_parquet("jobs.parquet", index=False)
employees_df.to_parquet("employees.parquet", index=False)

print("Archivos PARQUET generados exitosamente.")