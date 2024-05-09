from models.movie import Movie, movies_schema, movie_schema


class MovieService():
    def __init__(self, db):
        self.db = db

    def get_movies(self):
        all_movies = Movie.query.all()
        return movies_schema.dump(all_movies)

    def create_movie(self, movie):
        new_movie = Movie(
            title=movie['title'],
            overview=movie['overview'],
            year=movie['year'],
            rating=movie['rating'],
            image=movie['image']
        )
        self.db.session.add(new_movie)
        self.db.session.commit()
        return movie_schema.dump(new_movie)
