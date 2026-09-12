from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from starlette import status

import crud as url_service
from db import get_db
from schemas import URLCreate

url_router = APIRouter()

@url_router.post("/", status_code=status.HTTP_201_CREATED)
def create_url(url: URLCreate, session: Session = Depends(get_db)):
    return url_service.create_url(url, session)