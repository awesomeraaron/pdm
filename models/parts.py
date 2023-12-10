from sqlalchemy import *
from sqlalchemy.orm import relationship
from database import Base
from models.fitments import Fitment
from models.sku import SKU

class Part(Base):
    __tablename__ = 'parts'
    
    id = Column(Integer, primary_key=True)

    # note: 
    # 1. metadata is a reserved word
    # 2. depends on the usecase, it would be a JSON too
    # 3. the metadata here would be description/warming for a particular item with the particular fitment
    meta_data = Column(String)  
    
    sku_id = Column(Integer, ForeignKey('skus.id'))
    fitment_id = Column(Integer, ForeignKey('fitments.id'))

    fitment  = relationship(Fitment)
    sku  = relationship(SKU)

