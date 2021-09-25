from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = "Remote"
    company_url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[str] = datetime.now().date()


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class JobShow(JobBase):
    title: str
    company: str
    location: str
    description: Optional[str]
    company_url: Optional[str]
    date_posted: date

    class Config():
        orm_mode = True
