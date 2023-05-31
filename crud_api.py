from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 1, "title": "Spirited Away", "director": "Hayao Miyazaki", "release_year": 2001, "genre": "Adventure"},
    {"id": 2, "title": "A Silent Voice", "director": "Naoko Yamada", "release_year": 2016, "genre": "Drama"},
    {"id": 3, "title": "The Girl Who Lept Through Time", "director": "Mamoru Hosoda", "release_year": 2006, "genre": "Sci-Fi"},
    {"id": 4, "title": "Arriety", "director": "Hiromasa Yonebayashi", "release_year": 2010, "genre": "Fantasy"},
    {"id": 5, "title": "Your Name", "director": "Makoto Shinkai", "release_year": 2016, "genre": "Romance"},
]