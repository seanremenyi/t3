from main import ma
from models.Artists import Artists

class ArtistsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artists

artist_schema = ArtistsSchema()
artists_schema = ArtistsSchema(many=True)