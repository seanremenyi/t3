from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    db = SQLAlchemy(app)

    return db


# import psycopg2

# connection = psycopg2.connect(
#     database="spotify",
#     user="postgres",
#     password="postgres",
#     host="54.206.181.154"
# )

# cursor = connection.cursor()

# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
# connection.commit()