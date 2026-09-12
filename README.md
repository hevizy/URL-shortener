# Simple URL shorter 

It`s my first project on fastapi

**Backend Stack:**

_FastAPI_ - route logic (endpoints)

_SQLAlchemy_ - URL model in DB(SQLite)

_Alembic_ - DB migrations

_Hashids_ - generate unique string for short url

_uvicorn_

**Frontend Stack:**

React (vite), Axios

## Start

**db migrations**
```bash
cd backend
uv run alembic upgrade head
```

---
### Run API

```bash
uv run uvicorn app.main:app
```

_Server is going start on_ http://localhost:8000

---

### Run frontend
**In second terminal**

```bash
cd frontend
```



**Install dependents** 

```bash
npm install 
```

**Start interface**

```bash
npm run dev
```

_Server is going start on_ http://localhost:5173

---



