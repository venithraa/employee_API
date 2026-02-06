from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, crud
from app.database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI(
    title="Employee Management API - Assignment",
    description="RESTful API for Employee CRUD Operations",
    version="1.0.0",
)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Employee Management API",
        "docs": "/docs",
        "author": "Venithraa Ganesan",
    }

@app.post("/api/v1/employees", status_code=201, tags=["Employees"])
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee"""
    db_employee = crud.create_employee(db=db, employee=employee)
    
    # Manually convert to dict
    return {
        "success": True,
        "message": "Employee created successfully",
        "data": {
            "id": db_employee.id,
            "first_name": db_employee.first_name,
            "last_name": db_employee.last_name,
            "email": db_employee.email,
            "phone": db_employee.phone,
            "department": db_employee.department,
            "position": db_employee.position,
            "salary": db_employee.salary,
            "hire_date": str(db_employee.hire_date) if db_employee.hire_date else None,
            "created_at": str(db_employee.created_at),
            "updated_at": str(db_employee.updated_at) if db_employee.updated_at else None
        }
    }

@app.get("/api/v1/employees", tags=["Employees"])
def get_all_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all employees with pagination"""
    employees = crud.get_employees(db, skip=skip, limit=limit)
    
    # Convert list of employees to dicts
    employee_list = []
    for emp in employees:
        employee_list.append({
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "email": emp.email,
            "phone": emp.phone,
            "department": emp.department,
            "position": emp.position,
            "salary": emp.salary,
            "hire_date": str(emp.hire_date) if emp.hire_date else None,
            "created_at": str(emp.created_at),
            "updated_at": str(emp.updated_at) if emp.updated_at else None
        })
    
    return {
        "success": True,
        "message": "Employees retrieved successfully",
        "data": employee_list
    }

@app.get("/api/v1/employees/{employee_id}", tags=["Employees"])
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID"""
    emp = crud.get_employee(db, employee_id=employee_id)
    
    return {
        "success": True,
        "message": "Employee retrieved successfully",
        "data": {
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "email": emp.email,
            "phone": emp.phone,
            "department": emp.department,
            "position": emp.position,
            "salary": emp.salary,
            "hire_date": str(emp.hire_date) if emp.hire_date else None,
            "created_at": str(emp.created_at),
            "updated_at": str(emp.updated_at) if emp.updated_at else None
        }
    }

@app.put("/api/v1/employees/{employee_id}", tags=["Employees"])
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    """Update an existing employee"""
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    
    return {
        "success": True,
        "message": "Employee updated successfully",
        "data": {
            "id": db_employee.id,
            "first_name": db_employee.first_name,
            "last_name": db_employee.last_name,
            "email": db_employee.email,
            "phone": db_employee.phone,
            "department": db_employee.department,
            "position": db_employee.position,
            "salary": db_employee.salary,
            "hire_date": str(db_employee.hire_date) if db_employee.hire_date else None,
            "created_at": str(db_employee.created_at),
            "updated_at": str(db_employee.updated_at) if db_employee.updated_at else None
        }
    }

@app.delete("/api/v1/employees/{employee_id}", tags=["Employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete an employee"""
    result = crud.delete_employee(db, employee_id=employee_id)
    return result

@app.get("/api/v1/employees/search/query", tags=["Employees"])
def search_employees(keyword: str, db: Session = Depends(get_db)):
    """Search employees by keyword"""
    employees = crud.search_employees(db, keyword=keyword)
    
    employee_list = []
    for emp in employees:
        employee_list.append({
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "email": emp.email,
            "phone": emp.phone,
            "department": emp.department,
            "position": emp.position,
            "salary": emp.salary,
            "hire_date": str(emp.hire_date) if emp.hire_date else None,
            "created_at": str(emp.created_at),
            "updated_at": str(emp.updated_at) if emp.updated_at else None
        })
    
    return {
        "success": True,
        "message": "Search completed successfully",
        "data": employee_list
    }

@app.get("/api/v1/employees/department/{department}", tags=["Employees"])
def get_by_department(department: str, db: Session = Depends(get_db)):
    """Get employees by department"""
    employees = crud.get_by_department(db, department=department)
    
    employee_list = []
    for emp in employees:
        employee_list.append({
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "email": emp.email,
            "phone": emp.phone,
            "department": emp.department,
            "position": emp.position,
            "salary": emp.salary,
            "hire_date": str(emp.hire_date) if emp.hire_date else None,
            "created_at": str(emp.created_at),
            "updated_at": str(emp.updated_at) if emp.updated_at else None
        })
    
    return {
        "success": True,
        "message": f"Employees in {department} retrieved successfully",
        "data": employee_list
    }