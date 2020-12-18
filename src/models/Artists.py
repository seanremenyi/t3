from main import db

class Artists(db.Model):
    __tablename__ = "artists"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())