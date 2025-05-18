from fastapi import FastAPI
from .routers import medic, auth
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(medic.router)
app.include_router(auth.router)
@app.get("/")
async def root ():
    print('abv')
    return {"message": "Test World hahahhahha erorr"}

