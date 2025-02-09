from flask_sqlalchemy import SQLAlchemy

from app import db  # Import AFTER defining db in __init__.py

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
