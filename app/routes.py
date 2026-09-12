from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from starlette import status

import crud as url_service
from db import get_db
from schemas import URLCreate, URLResponse

url_router = APIRouter()

@url_router.post("/shortener", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_url(url: URLCreate, request: Request, session: Session = Depends(get_db)):
    """
    Get long url \
    :param url: \
    :param session: \
    :return: URLResponse (long_url, short_url, clicks) \
    """
    db_url = url_service.create_url(url, session)
    full_short_url = f"{request.base_url}{db_url.short_url}"
    return {
        "origin_url": db_url.origin_url,
        "short_url": full_short_url,
        "clicks": db_url.clicks
    }

@url_router.get("/{short_id}", status_code=status.HTTP_302_FOUND)
def redirect_by_short_url(short_id: str, session: Session = Depends(get_db)):
    db_url = url_service.get_url_by_short_id(short_id, session)
    if not db_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)
    db_url.clicks += 1
    session.commit()

    return RedirectResponse(url=db_url.origin_url)