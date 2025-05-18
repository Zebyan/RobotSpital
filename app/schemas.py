from pydantic import BaseModel, validator, ValidationError, EmailStr, Field
from typing import Optional


class CreatePacient(BaseModel):
    CNP: str
    nume: str
    prenume: str
    judet: str
    localitate: str
    strada: str
    nr_strada: int
    scara: Optional[str] = Field(default=None)
    apartament: Optional[int] = Field(default=None)
    telefon: str
    email: EmailStr
    profesie: Optional[str] = Field(default=None)
    loc_de_munca: Optional[str] = Field(default=None)
    sex: str
    grupa_sange: str
    rh: str
    id_pat: str

    @validator('CNP')
    def validate_cnp(cls, v):
        if v is not None:
            if len(v) != 13:
                raise ValueError("CNP nu are 13 cifre!")
            if not v.isdigit():
                raise ValueError("CNP contine doar cifre!")
        return v
        
    @validator('email')
    def validate_email(cls, v):
        if v is not None:
            if '@' not in v:
                raise ValueError('Email invalid')
        return v

    class Config:
        orm_mode = True


class UpdatePacient(BaseModel):
    CNP: Optional[str] = None
    nume: Optional[str] = None
    prenume: Optional[str] = None
    judet: Optional[str] = None
    localitate: Optional[str] = None
    strada: Optional[str] = None
    nr_strada: Optional[int] = None
    scara: Optional[str] = None
    apartament: Optional[int] = None
    telefon: Optional[str] = None
    email: Optional[EmailStr] = None
    profesie: Optional[str] = None
    loc_de_munca: Optional[str] = None
    sex: Optional[str] = None
    grupa_sange: Optional[str] = None
    rh: Optional[str] = None
    id_pat: Optional[str] = None

    class Config:
        orm_mode = True

class CreateAngajat(BaseModel):
    rol: str
    nume: str
    prenume: str
    email: EmailStr
    class Config:
        orm_mode: True

class AngajatLogin(BaseModel):
    username:EmailStr
    password: str
    rememberMe:Optional[ bool ] = False

class Token(BaseModel):
    access_token: str
    token_type: str

class Token_Data(BaseModel):
    rol:str
