from sqlalchemy import *
from database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    image_uri = Column(String)
