# app/main.py
from fastapi import FastAPI
from app import models, database, routes

app = FastAPI(
    title="Task Management System",
    description="A RESTful API for managing tasks",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=database.engine)

app.include_router(routes.router)