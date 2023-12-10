from models.parts import Part as PartModel
from models.fitments import Fitment as FitmentModel
from models.sku import SKU as SKUModel
from models.images import Image as ImageModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class Fitment(SQLAlchemyObjectType):
    class Meta:
        model = FitmentModel
        interfaces = (relay.Node,)


class SKU(SQLAlchemyObjectType):
    class Meta:
        model = SKUModel
        interfaces = (relay.Node,)


class Part(SQLAlchemyObjectType):
    class Meta:
        model = PartModel
        interfaces = (relay.Node,)

class Image(SQLAlchemyObjectType):
    class Meta:
        model = ImageModel
        interfaces = (relay.Node,)

# class OtherMetaData(SQLAlchemyObjectType):
#     class Meta:
#         model = OtherMetaDataModel
#         interfaces = (relay.Node,)

# class ShipmentPackaging(SQLAlchemyObjectType):
#     class Meta:
#         model = ShipmentPackagingModel
#         interfaces = (relay.Node,)

class ImageMutation(graphene.Mutation):
    class Arguments:
        image_uri = graphene.String(required=True)
    
    image = graphene.Field(lambda: Image)

    def mutate(self, info, image_uri):
        image = ImageModel(image_uri=image_uri)
        

        # add to DB
        from sqlalchemy.orm import scoped_session, sessionmaker
        from sqlalchemy import create_engine

        engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
        db_session = scoped_session(
            sessionmaker(bind=engine)
        )

        db_session.add(image)
        db_session.commit()

        return ImageMutation() 

class Mutation(graphene.ObjectType):
    mutate_image = ImageMutation.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_parts = SQLAlchemyConnectionField(Part.connection)

    all_fitments = SQLAlchemyConnectionField(Fitment.connection)

    all_sku = SQLAlchemyConnectionField(SKU.connection)
    
    all_images = SQLAlchemyConnectionField(Image.connection)

schema = graphene.Schema(query=Query, mutation=Mutation)