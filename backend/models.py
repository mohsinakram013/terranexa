from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    area = Column(Float, nullable=False)
    soil_type = Column(String, nullable=False)
    crop = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
class SoilRecord(Base):
    __tablename__ = "soil_records"

    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    nitrogen = Column(Float, nullable=False)
    phosphorus = Column(Float, nullable=False)
    potassium = Column(Float, nullable=False)
    ph = Column(Float, nullable=False)
    moisture = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    health_score = Column(Float, nullable=True)
Base.metadata.create_all(bind=engine)