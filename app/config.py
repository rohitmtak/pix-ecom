import os

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_NAME = "ecommerce_db"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
