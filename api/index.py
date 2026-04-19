from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.db.database import engine
from app.models.models import Base
from app.routers import auth, tasks

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager with JWT authentication",
    version="1.0.0",
)

# Enhanced CORS for Vercel
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://*.vercel.app",
    "http://*.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (consider restricting in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Task Manager API is running"}


# Export the app for Vercel
handler = app
