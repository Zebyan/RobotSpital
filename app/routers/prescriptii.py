from .. import models, schemas, oath2, utils
from fastapi import Depends, status, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(
    prefix = "/",
    tags = ["Prescriptii"]
)

