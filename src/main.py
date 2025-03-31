from fastapi import FastAPI
from src.routers.blacklist_routers import router as blacklist_router
from src.db.database import engine, Base  # 👈 Quita el punto

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blacklist Email Service")

app.include_router(blacklist_router)