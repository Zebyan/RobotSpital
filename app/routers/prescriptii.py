from .. import models, schemas, oath2, utils
from fastapi import Depends, status, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(
    prefix = "/prescriptii",
    tags = ["Prescriptii"]
)

@router.get("/", response_model=List[schemas.Prescriptii])
def vizualizare_pacienti(db: Session = Depends(get_db), access: schemas.Token_Data = Depends(oath2.get_current_angajat)):
    if not utils.verify_medic_rol(access.rol):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Nu aveti access!"
        )

    prescriptii = db.query(models.Prescriptii).all()
    return prescriptii



