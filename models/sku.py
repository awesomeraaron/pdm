from sqlalchemy import *
from database import Base
from models.images import Image

from sqlalchemy.orm import relationship


class SKU(Base):
    __tablename__ = "skus"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    sku_id = Column(Integer, unique=True)

    image_id = Column(Integer, ForeignKey("images.id"))
    image = relationship(Image)

    # attribute_id = Column(Integer, ForeignKey('attributes.id'))
    # shipment_packaging_id = Column(Integer, ForeignKey('shipment_packagings.id'))

    # attribute  = relationship(Attribute)
    # shipment_packaging = relationship(ShipmentPackaging)
