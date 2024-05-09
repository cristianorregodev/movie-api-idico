from utils.db import db, ma


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    overview = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    image = db.Column(db.String(255))

    def __init__(self, title, overview, year, rating, image):
        self.title = title
        self.overview = overview
        self.year = year
        self.rating = rating
        self.image = image


class MovieSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "overview", "year", "rating", "image")


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
