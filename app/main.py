from fastapi import FastAPI
from .routers import medic, auth
from .database import engine
from .models import Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],            # or a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],            # or specific ["GET", "POST", ...]
    allow_headers=["*"],            # or specific headers
)

app.include_router(medic.router)
app.include_router(auth.router)
@app.get("/")
async def root ():
    print('abv')
    return {"message": "Hello world v4.0"}

