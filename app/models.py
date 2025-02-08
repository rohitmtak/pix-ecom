from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)  # Category Name
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)  # URL-friendly name
