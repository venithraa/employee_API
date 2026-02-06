from fastapi.testclient import TestClient
from app.main import app
import random
import string

client = TestClient(app)

def random_email():
    """Generate a random email for testing"""
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}@example.com"

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee Management API"

def test_create_employee():
    """Test creating a valid employee"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "Engineering",
            "position": "Software Engineer",
            "salary": 50000,
            "hire_date": "2024-01-15"
        }
    )
    assert response.status_code == 201
    assert response.json()["success"] == True

def test_invalid_email():
    """Test validation for invalid email format"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": "notanemail",
            "phone": "9876543210",
            "department": "IT",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_invalid_phone():
    """Test validation for invalid phone number"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": random_email(),
            "phone": "123",
            "department": "IT",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_short_name():
    """Test validation for name that's too short"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "A",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "IT",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_string_as_first_name():
    """Test validation prevents 'string' as first name"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "string",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "IT",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_string_as_department():
    """Test validation prevents 'string' as department"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "string",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_string_as_position():
    """Test validation prevents 'string' as position"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "IT",
            "position": "string",
            "salary": 50000
        }
    )
    assert response.status_code == 422

def test_negative_salary():
    """Test validation for negative salary"""
    response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Test",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "IT",
            "position": "Developer",
            "salary": -1000
        }
    )
    assert response.status_code == 422

def test_get_employees():
    """Test getting all employees"""
    response = client.get("/api/v1/employees")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "success" in response.json()

def test_get_employee_by_id():
    """Test getting a specific employee by ID"""
    # First create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "GetTest",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "QA",
            "position": "Tester",
            "salary": 60000
        }
    )
    employee_id = create_response.json()["data"]["id"]
    
    # Then get it by ID
    response = client.get(f"/api/v1/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "GetTest"

def test_get_nonexistent_employee():
    """Test getting an employee that doesn't exist"""
    response = client.get("/api/v1/employees/99999")
    assert response.status_code == 404

def test_update_employee():
    """Test updating an employee"""
    # First create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "UpdateTest",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "Engineering",
            "position": "Junior Developer",
            "salary": 50000
        }
    )
    employee_id = create_response.json()["data"]["id"]
    
    # Update the employee
    response = client.put(
        f"/api/v1/employees/{employee_id}",
        json={
            "position": "Senior Developer",
            "salary": 80000
        }
    )
    assert response.status_code == 200
    assert response.json()["data"]["position"] == "Senior Developer"
    assert response.json()["data"]["salary"] == 80000

def test_delete_employee():
    """Test deleting an employee"""
    # First create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "first_name": "DeleteTest",
            "last_name": "User",
            "email": random_email(),
            "phone": "9876543210",
            "department": "Temporary",
            "position": "Intern",
            "salary": 40000
        }
    )
    employee_id = create_response.json()["data"]["id"]
    
    # Delete the employee
    response = client.delete(f"/api/v1/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["success"] == True
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/employees/{employee_id}")
    assert get_response.status_code == 404

def test_search_employees():
    """Test searching employees"""
    unique_keyword = ''.join(random.choices(string.ascii_lowercase, k=8))
    
    # Create a test employee with unique keyword
    client.post(
        "/api/v1/employees",
        json={
            "first_name": unique_keyword,
            "last_name": "Employee",
            "email": random_email(),
            "phone": "9876543210",
            "department": "QA",
            "position": "QA Engineer",
            "salary": 55000
        }
    )
    
    # Search for it
    response = client.get(f"/api/v1/employees/search/query?keyword={unique_keyword}")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0

def test_duplicate_email():
    """Test that duplicate emails are rejected"""
    email = random_email()
    
    # Create first employee
    response1 = client.post(
        "/api/v1/employees",
        json={
            "first_name": "First",
            "last_name": "User",
            "email": email,
            "phone": "9876543210",
            "department": "Engineering",
            "position": "Developer",
            "salary": 50000
        }
    )
    assert response1.status_code == 201
    
    # Try to create another with same email
    response2 = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Second",
            "last_name": "User",
            "email": email,  # Same email
            "phone": "9876543211",
            "department": "Sales",
            "position": "Sales Executive",
            "salary": 50000
        }
    )
    assert response2.status_code == 400

def test_duplicate_names_allowed():
    """Test that duplicate names are allowed (different emails)"""
    # Create first employee
    response1 = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Rajesh",
            "last_name": "Kumar",
            "email": random_email(),
            "phone": "9876543210",
            "department": "Engineering",
            "position": "Software Engineer",
            "salary": 70000
        }
    )
    assert response1.status_code == 201
    
    # Create second employee with same name but different email
    response2 = client.post(
        "/api/v1/employees",
        json={
            "first_name": "Rajesh",
            "last_name": "Kumar",
            "email": random_email(),  # Different email
            "phone": "9876543211",
            "department": "Sales",
            "position": "Sales Manager",
            "salary": 80000
        }
    )
    assert response2.status_code == 201  # Should succeed