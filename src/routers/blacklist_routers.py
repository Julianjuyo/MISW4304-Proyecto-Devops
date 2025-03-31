from fastapi import APIRouter, Depends, Header, HTTPException, Request, Path
from sqlalchemy.orm import Session
from src.db.database import get_db
from ..schemas.blacklist_schemas import BlacklistEmailCreate, BlacklistEmailResponse
from ..services.blacklist_services import add_email_to_blacklist, get_blacklist_status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import EmailStr

router = APIRouter(prefix="/blacklists", tags=["Blacklist"])
security = HTTPBearer()
STATIC_BEARER_TOKEN = "123456"

@router.post("/", status_code=201)
def add_email(
    email_data: BlacklistEmailCreate,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    if credentials.credentials != STATIC_BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    ip_address = request.client.host  
    return add_email_to_blacklist(db, email_data, ip_address)

@router.get("/{email}", response_model=BlacklistEmailResponse)
def check_email(
    email: EmailStr = Path(..., title="Email Address", description="Email to check in the blacklist"),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    if credentials.credentials != STATIC_BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    blacklisted_email = get_blacklist_status(db, email)
    if not blacklisted_email.is_blacklisted:
        raise HTTPException(status_code=404, detail="Email not found in blacklist")

    return blacklisted_email