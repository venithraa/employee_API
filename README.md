# Employee Management System - REST API

**Developer**: Venithraa Ganesan  
**Date**: February 6, 2026  
**Assignment**: Take-Home Assessment

---

## Quick Start
```bash
# Clone repository
git clone https://github.com/venithraa/employee_API.git
cd employee_API

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure database
# Copy .env.example to .env and update your MySQL password

# Create database
# CREATE DATABASE promon_employee_db;

# Run application
uvicorn app.main:app --reload

# Access Swagger UI
http://localhost:8000/docs
```

---

## Technology Stack

- **Framework**: FastAPI
- **Database**: MySQL 8.0
- **ORM**: SQLAlchemy 2.0
- **Validation**: Pydantic v2
- **Testing**: Pytest

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| POST | `/api/v1/employees` | Create employee |
| GET | `/api/v1/employees` | Get all employees |
| GET | `/api/v1/employees/{id}` | Get employee by ID |
| PUT | `/api/v1/employees/{id}` | Update employee |
| DELETE | `/api/v1/employees/{id}` | Delete employee |
| GET | `/api/v1/employees/search/query?keyword=x` | Search employees |
| GET | `/api/v1/employees/department/{dept}` | Filter by department |

---

## Database Schema
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10),
    department VARCHAR(50),
    position VARCHAR(50),
    salary FLOAT,
    hire_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);
```

---

## Features

- Complete CRUD operations
- Input validation (email, phone, names, salary)
- Unique email constraint
- Search functionality (name, email, department, position)
- Department filtering
- Pagination support
- Automatic Swagger documentation
- Error handling with proper HTTP status codes

---

## Validation Rules

**Names**: 2-50 characters, letters only, cannot be "string"  
**Email**: Valid format, must be unique  
**Phone**: Exactly 10 digits (optional)  
**Department/Position**: Min 2 characters, cannot be "string" (optional)  
**Salary**: Must be positive (optional)  

---

## Example Request

**Create Employee:**
```json
{
  "first_name": "Rajesh",
  "last_name": "Kumar",
  "email": "rajesh@example.com",
  "phone": "9876543210",
  "department": "Engineering",
  "position": "Software Engineer",
  "salary": 750000,
  "hire_date": "2024-01-15"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Employee created successfully",
  "data": {
    "id": 1,
    "first_name": "Rajesh",
    "last_name": "Kumar",
    "email": "rajesh@example.com",
    ...
  }
}
```

---

## Testing

Run automated tests:
```bash
pytest test/ -v
```

17 test cases covering CRUD operations, validation, error handling, and edge cases.

---

## Project Structure
```
employee_API/
├── app/
│   ├── main.py          # API routes
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── database.py      # DB connection
├── test/
│   └── test_main.py     # Test cases
├── .env.example         # Configuration template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Screenshots

**Swagger UI - All Endpoints:**

<img width="1351" height="656" alt="Screenshot 2026-02-06 103643" src="https://github.com/user-attachments/assets/adcf9f6e-2fb0-4855-8a02-571a45b1d645" />



**Successful POST Request (201 Created):**

<img width="1287" height="551" alt="Screenshot 2026-02-06 085106" src="https://github.com/user-attachments/assets/e99dcae1-9239-4500-954e-7155f892793c" />



**GET All Employees:**

<img width="1309" height="438" alt="Screenshot 2026-02-06 104225" src="https://github.com/user-attachments/assets/771babc2-cebc-4f5f-b922-433e8181faa0" />
<img width="1287" height="551" alt="Screenshot 2026-02-06 085106" src="https://github.com/user-attachments/assets/ccad53f8-8435-465f-ae94-e5a28c95ceca" />



**Validation Error (422):**

<img width="1264" height="628" alt="Screenshot 2026-02-06 104628" src="https://github.com/user-attachments/assets/a9b77db5-1911-43ae-991d-13d91222870c" />



**Duplicate Email Error (400):**

<img width="1260" height="336" alt="Screenshot 2026-02-06 085728" src="https://github.com/user-attachments/assets/bb02cae8-4abc-47a9-ada3-20e6ec1472b3" />



**Search Functionality:**

<img width="1356" height="569" alt="Screenshot 2026-02-06 104733" src="https://github.com/user-attachments/assets/55e9109e-ae6f-4717-9d21-12892d53a817" />
<img width="1307" height="561" alt="Screenshot 2026-02-06 104800" src="https://github.com/user-attachments/assets/1b833c1a-f75d-4eb1-b134-5d753180da11" />



**MySQL Database:**

<img width="1365" height="674" alt="Screenshot 2026-02-06 104945" src="https://github.com/user-attachments/assets/fb6915f5-37ea-4147-8e66-171274195c1d" />


---

**Repository**: https://github.com/venithraa/employee_API
