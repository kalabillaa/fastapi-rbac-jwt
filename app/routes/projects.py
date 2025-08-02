from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import Project
from app.database import get_session
from app.deps import get_current_user, get_admin_user

router = APIRouter()

@router.get("/projects")
def get_projects(session: Session = Depends(get_session), user=Depends(get_current_user)):
    return session.exec(select(Project)).all()

@router.post("/projects")
def create_project(project: Project, session: Session = Depends(get_session), user=Depends(get_admin_user)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
