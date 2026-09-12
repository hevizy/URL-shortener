from hashids import Hashids
from app.config import settings

hashids = Hashids(salt=settings.HASHID_SALT, min_length=6,)


def encode(db_id: int) -> str:
    return hashids.encode(db_id)