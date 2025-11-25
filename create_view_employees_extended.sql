CREATE VIEW IF NOT EXISTS vw_employees_extended AS
SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS full_name,
    e.email,
    e.hire_date,
    e.salary,
    j.job_title,
    d.department_name,
    d.location,
    
    CASE 
        WHEN e.salary < 4000 THEN 'Low'
        WHEN e.salary BETWEEN 4000 AND 7000 THEN 'Medium'
        ELSE 'High'
    END AS salary_level

FROM employees e
INNER JOIN jobs j 
    ON e.job_id = j.job_id
INNER JOIN departments d
    ON e.department_id = d.department_id;
