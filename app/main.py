from fastapi import FastAPI
import models
from db import engine
from routes import url_router

# models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(url_router)
@app.get("/root")
async def root():
    return {"message": "Hello World"}
