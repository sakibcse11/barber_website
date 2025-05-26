from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Optional
from datetime import datetime
import re


class BookingRequest(BaseModel):
    email: EmailStr
    name: str
    phone: str
    date: str  # YYYY-MM-DD format
    time: str  # HH:MM format
    service: Optional[str] = "general"

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        # Remove all non-digit characters for validation
        phone_digits = re.sub(r'\D', '', v)
        if len(phone_digits) < 10:
            raise ValueError('Phone number must be at least 10 digits')
        return v

    @field_validator('date')
    @classmethod
    def validate_date(cls, v: str) -> str:
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format')
        return v

    @field_validator('time')
    @classmethod
    def validate_time(cls, v: str) -> str:
        try:
            datetime.strptime(v, '%H:%M')
        except ValueError:
            raise ValueError('Time must be in HH:MM format')
        return v


class AvailabilityResponse(BaseModel):
    date: str
    available_times: List[str]
    success: bool = True
    message: Optional[str] = None


class BookingResponse(BaseModel):
    success: bool
    message: str
    booking_id: Optional[str] = None
    appointment_details: Optional[dict] = None


class HealthCheckResponse(BaseModel):
    status: str
    calendly_configured: bool
    timestamp: str