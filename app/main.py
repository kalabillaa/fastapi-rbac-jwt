from fastapi import FastAPI
from app.routes import users, projects
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(users.router)
app.include_router(projects.router)
