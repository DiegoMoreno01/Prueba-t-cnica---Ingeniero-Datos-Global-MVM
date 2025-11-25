import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "hr_data.db"

def query_view():
    conn = sqlite3.connect(DB_PATH)
    
    print("Creando vista vw_employees_extended...")

    # Leer archivo SQL y ejecutarlo
    sql_path = BASE_DIR / "create_view_employees_extended.sql"
    sql_script = sql_path.read_text()

    conn.executescript(sql_script)

    print("\nVista creada correctamente.\n")

    # Probar consulta
    cursor = conn.execute("""
        SELECT employee_id, full_name, job_title, department_name, salary_level
        FROM vw_employees_extended
        LIMIT 10;
    """)

    print("Ejemplo de datos:")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    query_view()
