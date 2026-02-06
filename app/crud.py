from sqlalchemy.orm import Session
from sqlalchemy import or_
from app import models, schemas
from fastapi import HTTPException

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    # Check if email exists
    existing_employee = db.query(models.Employee).filter(models.Employee.email == employee.email).first()
    if existing_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new employee
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    update_data = employee.model_dump(exclude_unset=True)
    
    # Check email uniqueness if being updated
    if "email" in update_data and update_data["email"] != db_employee.email:
        existing = db.query(models.Employee).filter(models.Employee.email == update_data["email"]).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(db_employee)
    db.commit()
    return {"success": True, "message": "Employee deleted successfully"}

def search_employees(db: Session, keyword: str):
    """Search employees by keyword in name, email, department, or position"""
    return db.query(models.Employee).filter(
        or_(
            models.Employee.first_name.ilike(f"%{keyword}%"),
            models.Employee.last_name.ilike(f"%{keyword}%"),
            models.Employee.email.ilike(f"%{keyword}%"),
            models.Employee.department.ilike(f"%{keyword}%"),
            models.Employee.position.ilike(f"%{keyword}%")
        )
    ).all()

def get_by_department(db: Session, department: str):
    """Get all employees in a specific department"""
    return db.query(models.Employee).filter(models.Employee.department == department).all()

def get_by_position(db: Session, position: str):
    """Get all employees with a specific position"""
    return db.query(models.Employee).filter(models.Employee.position == position).all()