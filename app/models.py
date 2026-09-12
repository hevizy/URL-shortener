from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from db import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(String, index=True)
    short_url = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    clicks = Column(Integer, default=0)

