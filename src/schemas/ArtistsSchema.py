from main import ma
from models.Artists import Artists
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class ArtistsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artists

    title = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)
    
    
artist_schema = ArtistsSchema()
artists_schema = ArtistsSchema(many=True)