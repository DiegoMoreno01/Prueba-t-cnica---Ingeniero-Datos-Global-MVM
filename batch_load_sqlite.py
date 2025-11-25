import pandas as pd
import sqlite3
from pathlib import Path

# Ruta base (directorio donde está este script)
BASE_DIR = Path(__file__).resolve().parent

# Rutas de archivos CSV
DEPARTMENTS_CSV = BASE_DIR / "departments.csv"
JOBS_CSV = BASE_DIR / "jobs.csv"
EMPLOYEES_CSV = BASE_DIR / "employees.csv"

# Ruta de la base de datos SQLite
DB_PATH = BASE_DIR / "hr_data.db"


def load_csv_to_sqlite():
    print("Iniciando proceso batch de carga a SQLite...\n")

    # Leer CSV con pandas
    departments_df = pd.read_csv(DEPARTMENTS_CSV)
    jobs_df = pd.read_csv(JOBS_CSV)
    employees_df = pd.read_csv(EMPLOYEES_CSV)

    # Conectarse / crear base SQLite
    conn = sqlite3.connect(DB_PATH)

    try:
        # Habilitar claves foráneas (por buenas prácticas)
        conn.execute("PRAGMA foreign_keys = ON;")

        # Cargar data a tablas (full load, reemplaza cada vez)
        departments_df.to_sql("departments", conn, if_exists="replace", index=False)
        jobs_df.to_sql("jobs", conn, if_exists="replace", index=False)
        employees_df.to_sql("employees", conn, if_exists="replace", index=False)

        # Crear índices básicos para mejorar consultas
        conn.execute("CREATE INDEX IF NOT EXISTS idx_jobs_department ON jobs(department_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_emp_department ON employees(department_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_emp_job ON employees(job_id);")

        conn.commit()

        print("Carga completada.")
        print(f"Base de datos creada en: {DB_PATH}\n")

        # Mostrar conteo de registros por tabla
        for table in ["departments", "jobs", "employees"]:
            cur = conn.execute(f"SELECT COUNT(*) FROM {table}")
            count = cur.fetchone()[0]
            print(f"Tabla {table}: {count} registros")

    finally:
        conn.close()
        print("\nConexión a SQLite cerrada.")


if __name__ == "__main__":
    load_csv_to_sqlite()