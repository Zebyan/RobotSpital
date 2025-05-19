from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, utils, oath2, schemas
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    tags=['Login']
)

@router.post('/login')
def login (date_angajat: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    db_angajat = db.query(models.Angajati).filter(models.Angajati.email == date_angajat.username).first()
    if not db_angajat: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Utilizatorul sau parola nu exista!")
    
    if not utils.verify_password(date_angajat.password, db_angajat.parola): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Utilizatorul sau parola nu exista!")

    access_token = oath2.create_access_token(data = {"rol": db_angajat.rol, "nume": db_angajat.nume})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/angajati", status_code=status.HTTP_201_CREATED)
def create_angajat(angajat: schemas.CreateAngajat,db: Session = Depends(database.get_db)):
    random_password = utils.generate_password()
    print(random_password)
    hashed_password = utils.get_password_hash(random_password)

    db_angajat = models.Angajati(rol = angajat.rol,
                                 nume = angajat.nume,
                                 prenume = angajat.prenume,
                                 email = angajat.email,
                                 parola = hashed_password)
    db.add(db_angajat)
    try:
        db.commit()
        db.refresh(db_angajat)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email deja folosit!")
    return db_angajat