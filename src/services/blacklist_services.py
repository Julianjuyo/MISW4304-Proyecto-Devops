from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.blacklist_model import BlacklistEmail
from ..schemas.blacklist_schemas import BlacklistEmailCreate, BlacklistEmailResponse
from datetime import datetime
import socket

def add_email_to_blacklist(db: Session, email_data: BlacklistEmailCreate, ip_address: str):
    existing_email = db.query(BlacklistEmail).filter(BlacklistEmail.email == email_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email is already in blacklist")

    new_blacklist_entry = BlacklistEmail(
        email=email_data.email,
        app_uuid=email_data.app_uuid,
        blocked_reason=email_data.blocked_reason,
        ip_address=ip_address,
        created_at=datetime.utcnow()
    )
    db.add(new_blacklist_entry)
    db.commit()
    db.refresh(new_blacklist_entry)
    return {"message": "Email successfully added to blacklist"}


def get_blacklist_status(db: Session, email: str):
    blacklisted_email = db.query(BlacklistEmail).filter(BlacklistEmail.email == email).first()
    if not blacklisted_email:
        return BlacklistEmailResponse(email=email, is_blacklisted=False, blocked_reason=None, created_at=datetime.utcnow())

    return BlacklistEmailResponse(
        email=blacklisted_email.email,
        is_blacklisted=True,
        blocked_reason=blacklisted_email.blocked_reason,
        created_at=blacklisted_email.created_at
    )