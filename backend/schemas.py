from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class FarmCreate(BaseModel):
    name: str
    location: str
    area: float
    soil_type: str
    crop: str

class FarmOut(BaseModel):
    id: int
    name: str
    location: str
    area: float
    soil_type: str
    crop: str
    owner_id: int

    class Config:
        from_attributes = True

class SoilCreate(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    moisture: float
    temperature: float

class SoilOut(BaseModel):
    id: int
    farm_id: int
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    moisture: float
    temperature: float
    health_score: float

    class Config:
        from_attributes = True

class CropRequest(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    temperature: float
    humidity: float
    rainfall: float