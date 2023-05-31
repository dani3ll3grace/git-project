import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

movies = [
    {"id": 1, "title": "Spirited Away", "director": "Hayao Miyazaki", "release_year": 2001, "genre": "Adventure"},
    {"id": 2, "title": "A Silent Voice", "director": "Naoko Yamada", "release_year": 2016, "genre": "Drama"},
    {"id": 3, "title": "The Girl Who Lept Through Time", "director": "Mamoru Hosoda", "release_year": 2006, "genre": "Sci-Fi"},
    {"id": 4, "title": "Arriety", "director": "Hiromasa Yonebayashi", "release_year": 2010, "genre": "Fantasy"},
    {"id": 5, "title": "Your Name", "director": "Makoto Shinkai", "release_year": 2016, "genre": "Romance"},
]

@app.route('/student')
def students():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student")
        studentRows = cursor.fetchall()
        respone = jsonify(studentRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = next((movie for movie in movies if movie["id"] == id), None)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({"message": "Movie not found"}), 404
    
@app.route('/movies', methods=['POST'])
def create_movie():
    new_movie = {
        "id": request.json["id"],
        "title": request.json["title"],
        "director": request.json["director"],
        "release_year": request.json["release_year"],
        "genre": request.json["genre"]
    }
    movies.append(new_movie)
    return jsonify({"message": "Movie created successfully"})

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = next((movie for movie in movies if movie["id"] == id), None)
    if movie:
        movie["title"] = request.json.get("title", movie["title"])
        movie["director"] = request.json.get("director", movie["director"])
        movie["release_year"] = request.json.get("release_year", movie["release_year"])
        movie["genre"] = request.json.get("genre", movie["genre"])
        return jsonify({"message": "Movie updated successfully"})
    else:
        return jsonify({"message": "Movie not found"}), 404

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = next((movie for movie in movies if movie["id"] == id), None)
    if movie:
        movies.remove(movie)
        return jsonify({"message": "Movie deleted successfully"})
    else:
        return jsonify({"message": "Movie not found"}), 404

if __name__ == '__main__':
    app.run()