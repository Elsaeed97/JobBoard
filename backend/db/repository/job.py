from fastapi.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from db.models.jobs import Job
from db.schemas.jobs import JobCreate
from sqlalchemy.orm import Session


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retrieve_job(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def list_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs


def update_job(id: int, job: JobCreate, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_job(id: int, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1
