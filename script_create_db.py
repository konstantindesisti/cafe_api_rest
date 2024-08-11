from movies import db, create_app
from movies.models import Movie


def create_database():
    app = create_app()
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_database()