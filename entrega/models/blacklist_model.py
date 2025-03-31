from sqlalchemy import Column, String, DateTime
from datetime import datetime
from ..db.database import Base

class BlacklistEmail(Base):
    __tablename__ = "blacklist_emails"

    email = Column(String, primary_key=True, index=True)
    app_uuid = Column(String, nullable=False, index=True)
    blocked_reason = Column(String, nullable=True)
    ip_address = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)