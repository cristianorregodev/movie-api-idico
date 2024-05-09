from flask import Flask
from flask_cors import CORS
from utils.db import db, ma
from routes.movies import movies


app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:codev@localhost/movies"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
ma.init_app(app)


app.register_blueprint(movies)
