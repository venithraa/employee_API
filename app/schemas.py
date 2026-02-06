from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from datetime import date, datetime
from typing import Optional, Any
import re

class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, description="Employee's first name")
    last_name: str = Field(..., min_length=2, max_length=50, description="Employee's last name")
    email: EmailStr = Field(..., description="Valid email address (must be unique)")
    phone: Optional[str] = Field(None, pattern=r"^\d{10}$", description="10-digit Indian phone number")
    department: Optional[str] = Field(None, max_length=50, description="Department name")
    position: Optional[str] = Field(None, max_length=50, description="Job position/title")
    salary: Optional[float] = Field(None, gt=0, description="Annual salary in INR (must be positive)")
    hire_date: Optional[date] = Field(None, description="Date of joining (YYYY-MM-DD)")

    @field_validator('first_name', 'last_name', 'department', 'position')
    @classmethod
    def validate_text_fields(cls, v, info):
        # Allow None for optional fields
        if v is None:
            return v
        
        v_stripped = v.strip()
        
        # Check if value is "string"
        if v_stripped.lower() == 'string':
            field_name = info.field_name.replace('_', ' ').title()
            raise ValueError(f'{field_name} cannot be "string". Please enter a real {info.field_name.replace("_", " ")}.')
        
        # For first_name and last_name: must be letters only
        if info.field_name in ['first_name', 'last_name']:
            if not re.match(r'^[A-Za-z\s]+$', v_stripped):
                raise ValueError('Name must contain only letters and spaces')
            
            letters_only = re.sub(r'\s', '', v_stripped)
            if len(letters_only) < 2:
                raise ValueError('Name must have at least 2 letters')
        
        # For department and position: at least 2 characters
        if info.field_name in ['department', 'position']:
            if len(v_stripped) < 2:
                raise ValueError(f'{info.field_name.title()} must be at least 2 characters')
        
        return v_stripped

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r"^\d{10}$")
    department: Optional[str] = Field(None, max_length=50)
    position: Optional[str] = Field(None, max_length=50)
    salary: Optional[float] = Field(None, gt=0, description="Annual salary in INR")
    hire_date: Optional[date] = None

    @field_validator('first_name', 'last_name', 'department', 'position')
    @classmethod
    def validate_text_fields(cls, v, info):
        if v is None:
            return v
            
        v_stripped = v.strip()
        
        if v_stripped.lower() == 'string':
            field_name = info.field_name.replace('_', ' ').title()
            raise ValueError(f'{field_name} cannot be "string". Please enter a real {info.field_name.replace("_", " ")}.')
        
        if info.field_name in ['first_name', 'last_name']:
            if not re.match(r'^[A-Za-z\s]+$', v_stripped):
                raise ValueError('Name must contain only letters and spaces')
            
            letters_only = re.sub(r'\s', '', v_stripped)
            if len(letters_only) < 2:
                raise ValueError('Name must have at least 2 letters')
        
        if info.field_name in ['department', 'position']:
            if len(v_stripped) < 2:
                raise ValueError(f'{info.field_name.title()} must be at least 2 characters')
        
        return v_stripped

class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None