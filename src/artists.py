from database import cursor, connection
from flask import Blueprint, request, jsonify
artists = Blueprint('artists', __name__, url_prefix="/artists")


@artists.route("/", methods=["GET"])
def book_index():
    #Return all books
    sql = "SELECT * FROM artists"
    cursor.execute(sql)
    artist = cursor.fetchall()
    return jsonify(artist)

@artists.route("/", methods=["POST"])
def book_create():
    #Create a new artists
    sql = "INSERT INTO artists (name) VALUES (%s);"
    cursor.execute(sql, (request.json["name"],))
    connection.commit()

    sql = "SELECT * FROM artists ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    artist = cursor.fetchone()
    return jsonify(artist)

@artists.route("/<int:id>", methods=["GET"])
def artists_show(id):
    #Return a single artists
    sql = "SELECT * FROM artists WHERE id = %s;"
    cursor.execute(sql, (id,))
    artist = cursor.fetchone()
    return jsonify(artist)

@artists.route("/<int:id>", methods=["PUT", "PATCH"])
def artists_update(id):
    #Update a artists
    sql = "UPDATE artists SET name = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["name"], id))
    connection.commit()

    sql = "SELECT * FROM artists WHERE id = %s"
    cursor.execute(sql, (id,))
    artist = cursor.fetchone()
    return jsonify(artist)

@artists.route("/<int:id>", methods=["DELETE"])
def artists_delete(id):
    sql = "SELECT * FROM artists WHERE id = %s;"
    cursor.execute(sql, (id,))
    artist = cursor.fetchone()
    
    if artist:
        sql = "DELETE FROM artists WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(artist)