from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app(configuration=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
