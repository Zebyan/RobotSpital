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
def vizualizare_prescriptii(db: Session = Depends(get_db), access: schemas.Token_Data = Depends(oath2.get_current_angajat)):
    if not utils.verify_medic_rol(access.rol):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Nu aveti access!"
        )

    prescriptii = db.query(models.Prescriptii).all()
    return prescriptii

@router.post("/", status_code=status.HTTP_201_CREATED)
def adaugare_prescriptie(prescriptii: schemas.Creare_Prescriptii, db: Session = Depends(get_db), 
                     access: schemas.Token_Data = Depends(oath2.get_current_angajat)):
    
    if not utils.verify_medic_rol(access.rol):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Nu aveti access!"
        )

    exist_prescriptii = db.query(models.Prescriptii).filter(models.Prescriptii.id_prescriptie == prescriptii.id_prescriptie).first()
    if exist_prescriptii:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pacientul deja exista!"
        )
    db_prescriptii = models.Prescriptii(id_prescriptie= prescriptii.id_prescriptie, 
                              cantitate = prescriptii.cantitate,
                              CNP = prescriptii.CNP,
                              afectiune = prescriptii.afectiune,
                              id_medicament = prescriptii.id_medicament
                              )
    
    print(access)
    db.add(db_prescriptii)
    db.commit()
    db.refresh(db_prescriptii)
    return {"message":"Prescriptia a fost creata!"}

