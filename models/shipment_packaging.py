from sqlalchemy import *
from database import Base
from sqlalchemy.orm import relationship

class ShipmentPackaging(Base):
    __tablename__ = "shipment_packaging"

    id  = Column(Integer, primary_key=True)
    fragile = Column(Boolean)
    hazardous = Column(String)
    size = Column(String)
    weight = Column(Float)

