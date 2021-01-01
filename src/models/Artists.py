from main import db

class Artists(db.Model):
    __tablename__ = "artists"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __repr__(self):
        return f"<Artists {self.title}>"