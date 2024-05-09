from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models.movie import Movie, movies_schema
from services.movie import MovieService
from utils.db import db

movies = Blueprint('movies', __name__)


@cross_origin
@movies.route("/movies", methods=["GET"])
def get_movies():
    result = MovieService(db).get_movies()
    result.reverse()
    return jsonify({"series": result}), 200


@cross_origin
@movies.route("/movies", methods=["POST"])
def create_movie():
    result = MovieService(db).create_movie(request.json)
    return jsonify({"serie_id": result['id']}), 201
