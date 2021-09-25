from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, session
from sqlalchemy.sql.expression import delete, update
from db.session import get_db
from db.repository.job import create_new_job, retrieve_job, list_jobs, update_job, delete_job
from db.schemas.jobs import JobCreate, JobShow

router = APIRouter()


@router.post("/create-job", response_model=JobShow)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get("/job/{id}", response_model=JobShow)
def retrieve_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does'nt exists")
    return job


@router.get("/all")
def list_all_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db)
    return jobs


@router.put("/update/{id}")
def update_job_by_id(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job_to_update = update_job(id=id, job=job, db=db, owner_id=owner_id)
    if not job_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does'nt exists")
    return {"details": "Successfully updated"}


@router.delete("delete/{id}")
def delete_job_by_id(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    job_to_delete = delete_job(id=id, db=db, owner_id=owner_id)
    if not job_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does'nt exists")
    return {"details": "Successfully Deleted"}
