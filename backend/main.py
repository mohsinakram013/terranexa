from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import auth
from soil_logic import calculate_soil_health
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to TerraNexa API"}

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = auth.hash_password(user.password)
    new_user = models.User(name=user.name, email=user.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful", "user_id": db_user.id}
@app.post("/farms", response_model=schemas.FarmOut)
def create_farm(farm: schemas.FarmCreate, owner_id: int, db: Session = Depends(get_db)):
    new_farm = models.Farm(
        name=farm.name,
        location=farm.location,
        area=farm.area,
        soil_type=farm.soil_type,
        crop=farm.crop,
        owner_id=owner_id
    )
    db.add(new_farm)
    db.commit()
    db.refresh(new_farm)
    return new_farm

@app.get("/farms/{owner_id}")
def get_farms(owner_id: int, db: Session = Depends(get_db)):
    farms = db.query(models.Farm).filter(models.Farm.owner_id == owner_id).all()
    return farms
@app.post("/soil-analysis/{farm_id}", response_model=schemas.SoilOut)
def create_soil_record(farm_id: int, soil: schemas.SoilCreate, db: Session = Depends(get_db)):
    score = calculate_soil_health(
        soil.nitrogen,
        soil.phosphorus,
        soil.potassium,
        soil.ph,
        soil.moisture,
        soil.temperature
    )

    new_record = models.SoilRecord(
        farm_id=farm_id,
        nitrogen=soil.nitrogen,
        phosphorus=soil.phosphorus,
        potassium=soil.potassium,
        ph=soil.ph,
        moisture=soil.moisture,
        temperature=soil.temperature,
        health_score=score
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record