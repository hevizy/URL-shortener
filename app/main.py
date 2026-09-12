from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import url_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_router)
@app.get("/root/")
async def root():
    return {"message": "Hello World"}
