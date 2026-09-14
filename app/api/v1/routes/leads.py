from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr


router = APIRouter()


class LeadCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None
    source: Literal["website", "telegram", "form", "api"]
    message: str


@router.post("/leads", status_code=201)
def create_lead(lead: LeadCreate):
    return {
        "message": "Lead accepted",
        "lead": lead
    }
