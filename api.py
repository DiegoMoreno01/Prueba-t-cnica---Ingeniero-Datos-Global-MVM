from fastapi import FastAPI
import sqlite3
from pathlib import Path

app = FastAPI(title="MVM HR API", version="1.0")

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "hr_data.db"


# Función para obtener conexión (buena práctica)
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn



# ENDPOINT PRINCIPAL

@app.get("/")
def root():
    return {"message": "API de Recursos Humanos - Global MVM"}



# EMPLOYEES

@app.get("/employees")
def get_employees():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM vw_employees_extended").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM vw_employees_extended WHERE employee_id = ?",
        (employee_id,)
    ).fetchone()
    conn.close()

    if row:
        return dict(row)
    return {"error": "Employee not found"}


@app.get("/employees/high-salary")
def get_high_salary_employees():
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM vw_employees_extended WHERE salary_level = 'High'"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]



# DEPARTMENTS

@app.get("/departments")
def get_departments():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM departments").fetchall()
    conn.close()
    return [dict(row) for row in rows]



# JOBS

@app.get("/jobs")
def get_jobs():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM jobs").fetchall()
    conn.close()
    return [dict(row) for row in rows]
