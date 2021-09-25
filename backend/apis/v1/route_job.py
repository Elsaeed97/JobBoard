from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.job import create_new_job
from db.schemas.jobs import JobCreate, JobShow

router = APIRouter()


@router.post("/create-job", response_model=JobShow)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job
