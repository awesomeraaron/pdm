from sqlalchemy import *
from database import Base


class Fitment(Base):
    __tablename__ = "fitments"

    id = Column(Integer, primary_key=True)
    maker = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
