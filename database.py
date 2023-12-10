from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """Init DB with some fake data for testing."""

    from models.parts import Part
    from models.fitments import Fitment
    from models.sku import SKU
    from models.images import Image

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    front_brake_image = Image(
        image_uri="https://www.istockphoto.com/photos/brake", id=333
    )
    db_session.add(front_brake_image)
    rear_brake_image = Image(
        image_uri="https://www.istockphoto.com/photos/brake2", id=334
    )
    db_session.add(rear_brake_image)
    general_wheel_image = Image(
        image_uri="https://www.vectorstock.com/royalty-free-vector/wheel-vector-125901",
        id=222,
    )
    db_session.add(general_wheel_image)
    race_wheel_image = Image(
        image_uri="https://www.pixelsquid.com/png/race-car-wheel-934829177079600848",
        id=111,
    )
    db_session.add(race_wheel_image)
    carbon_wheel_image = Image(
        image_uri="https://www.vectorstock.com/royalty-free-vector/wheel-vector-12331",
        id=000,
    )
    db_session.add(carbon_wheel_image)

    rear_brake = SKU(
        name="rear_brake",
        price=899,
        sku_id="0001",
        description="AWWWWW Stop",
        image_id=rear_brake_image.id,
    )
    db_session.add(rear_brake)
    front_brake = SKU(
        name="front_brake",
        price=799,
        sku_id="0002",
        description="Stop for good",
        image_id=front_brake_image.id,
    )
    db_session.add(front_brake)

    general_wheel = SKU(
        name="general_wheel",
        price=1000,
        sku_id="1003",
        description="Regular wheel",
        image_id=general_wheel_image.id,
    )
    db_session.add(general_wheel)
    race_wheel = SKU(
        name="race_wheel",
        price=2000,
        sku_id="1004",
        description="Cool wheel",
        image_id=race_wheel_image.id,
    )
    db_session.add(race_wheel)
    carbon_wheel = SKU(
        name="carbon_wheel",
        price=3000,
        sku_id="1005",
        description="Expansive wheel",
        image_id=carbon_wheel_image.id,
    )
    db_session.add(carbon_wheel)

    rav4_hybrid = Fitment(maker="Toyota", model="RAV4", year=2023)
    db_session.add(rav4_hybrid)
    rav4_gas = Fitment(maker="Toyota", model="RAV4", year=2019)
    db_session.add(rav4_gas)

    x3_hybrid = Fitment(maker="BMW", model="X3", year=2023)
    db_session.add(x3_hybrid)
    x3_gas = Fitment(maker="BMW", model="X3", year=2013)
    db_session.add(x3_gas)
    db_session.commit()

    for _car in [x3_hybrid, rav4_hybrid]:
        for _wheel in [general_wheel, race_wheel, carbon_wheel]:
            part = Part(
                meta_data="wheel matching", fitment_id=_car.id, sku_id=_wheel.id
            )
            db_session.add(part)

    for _car in [x3_gas, x3_hybrid, rav4_hybrid]:
        for _brake in [rear_brake, front_brake]:
            part = Part(
                meta_data="brake matching", fitment_id=_car.id, sku_id=_brake.id
            )
            db_session.add(part)

    db_session.commit()
