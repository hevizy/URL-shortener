# Simple URL shortener

1st fastapi project

<img width="1451" height="605" alt="image" src="https://github.com/user-attachments/assets/53be9384-6e68-454f-962e-c0a3aeeb7e53" />


**Backend Stack:**

_FastAPI_ - route logic (endpoints)

_SQLAlchemy_ - URL model in DB(SQLite)

_Alembic_ - DB migrations

_Hashids_ - generate unique string for short url

_uvicorn_ - ASGI web server

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

_API will be available at_ http://localhost:8000

---

### Run frontend
**In second terminal**

```bash
cd frontend
```



**Install dependencies** 

```bash
npm install 
```

**Start interface**

```bash
npm run dev
```

_Server will start at_ http://localhost:5173

---



