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

![Swagger UI Homepage](https://github.com/user-attachments/assets/70c960ec-09af-4412-b95b-5f00bcc9ee76)

**Successful POST Request (201 Created):**

![POST Success](https://github.com/user-attachments/assets/18dfdef4-67ae-4e84-be42-1aafcce51a89)

**GET All Employees:**

![GET All](https://github.com/user-attachments/assets/ea2427b0-4bcb-452f-9e03-11bbff259551)

**Validation Error (422):**

![Validation Error](https://github.com/user-attachments/assets/32d0e2ad-1e8a-4f40-837c-3ef491c90e55)

**Duplicate Email Error (400):**

![Duplicate Email](https://github.com/user-attachments/assets/cb8edf92-d5ed-4e04-bd50-b7e9d0dfdc53)

**Search Functionality:**

![Search](https://github.com/user-attachments/assets/02bd6634-505a-4ea6-bc92-4e763ef1d5dc)

**MySQL Database:**

![MySQL Data](https://github.com/user-attachments/assets/a3455a0f-3ec5-4d14-9fc9-71ec2654e406)

---

## Configuration

Create `.env` file:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/promon_employee_db
```

---

## Contact

**Venithraa Ganesan**  
Email: venithraaganesan@gmail.com  
Phone: +91 6281339264

---

**Repository**: https://github.com/venithraa/employee_API
