from sqlalchemy import *
from database import Base
from sqlalchemy.orm import relationship

class Fitment(Base):
    __tablename__ = "fitments"
    
    id  = Column(Integer, primary_key=True)
    maker = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    # sku = relationship('skus', secondary="parts", backref='fitments')
