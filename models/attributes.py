from sqlalchemy import *
from database import Base
from sqlalchemy.orm import relationship
import enum

class ColorEnum(enum.Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class SizeEnum(enum.Enum):
    SMALL = 1
    LARGE = 2


class Attribute(Base):
    __tablename__ = "attribute"
    
    id  = Column(Integer, primary_key=True)
    color = Column(Enum(ColorEnum))
    size = Column(Enum(SizeEnum))
    
