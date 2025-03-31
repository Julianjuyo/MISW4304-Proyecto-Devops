from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class BlacklistEmailCreate(BaseModel):
    email: EmailStr
    app_uuid: str
    blocked_reason: Optional[str] = None

class BlacklistEmailResponse(BaseModel):
    email: EmailStr
    is_blacklisted: bool
    blocked_reason: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True