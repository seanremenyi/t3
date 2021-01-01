from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")
    
@db_commands.cli.command("seed")
def seed_db():
    from models.Artists import Artists
    from models.User import User
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    # users = []

    # for i in range(5):
    #     user = User()
    #     user.email = f"test{i}@test.com"
    #     user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
    #     db.session.add(user)
    #     users.append(user)

    # db.session.commit()

    for i in range(20):
        artist = Artists()
        artist.name = faker.catch_phrase()
        db.session.add(artist)
    
    db.session.commit()
    print("Tables seeded")