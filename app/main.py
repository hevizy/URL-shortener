from fastapi import FastAPI
from app.routes import url_router


app = FastAPI()

app.include_router(url_router)
@app.get("/root/")
async def root():
    return {"message": "Hello World"}
