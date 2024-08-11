import os
from dotenv import load_dotenv


class Config:
    load_dotenv('../.env')
    SECRET_KEY = os.getenv('SECRET_KEY')
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(ROOT_PATH, 'movie_database.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH


