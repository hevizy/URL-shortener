from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl, ConfigDict

class URLCreate(BaseModel):
    url: HttpUrl

class URLInfo(BaseModel):
    id: int
    origin_url: HttpUrl
    short_url: HttpUrl
    date_created: datetime
    clicks: int

    model_config = ConfigDict(from_attributes=True)

class URLResponse(BaseModel):
    origin_url: HttpUrl
    short_url: HttpUrl
    clicks: int
