from fastapi import FastAPI
from . import models
from .database import engine
from .routers import medic, auth

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(medic.router)
app.include_router(auth.router)
@app.get("/")
async def root ():
    print('abv')
    return {"message": "Hello Man"}



