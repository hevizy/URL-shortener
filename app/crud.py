from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import URLCreate
from models import URL
from utils import encode


def create_url(url: URLCreate, session: Session, ):
    db_url = URL(
        origin_url=str(url.url),
    )

    exists = session.execute(
        select(URL).where(URL.origin_url == db_url.origin_url)
    ).scalar_one_or_none()
    if exists:
        return exists

    try:
        session.add(db_url)
        session.commit()
        session.refresh(db_url)
    except Exception as err:
        session.rollback()
        raise err

    short_url = encode(db_url.id)
    db_url.short_url = short_url

    try:
        session.add(db_url)
        session.commit()
        session.refresh(db_url)
    except Exception as err:
        session.rollback()
        raise err

    return db_url
