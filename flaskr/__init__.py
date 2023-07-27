import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    if test_config is None:
        load_dotenv(".flaskenv")

    app = Flask(__name__)
    app.config.from_object(f"config.{os.environ['APP_CONFIG']}")

    app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        db.init_app(app)

    with app.app_context():
        from flaskr.races import races_bp
        app.register_blueprint(races_bp, url_prefix='/races')
        if test_config is None:
            db.create_all()

    return app
