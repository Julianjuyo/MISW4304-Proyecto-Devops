from fastapi import FastAPI
from src.routers.blacklist_routers import router as blacklist_router
from src.routers.health_check_router import health_check_router
from src.db.database import engine, Base 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blacklist Email Service")

app.include_router(blacklist_router)
app.include_router(health_check_router)