from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS  # ✅ Import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load config from config.py
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from app import models  # Import models after app is created

    return app

app = create_app()
