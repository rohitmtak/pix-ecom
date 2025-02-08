from flask import Flask
from models import db
import config

app = Flask(__name__)

# Load MySQL Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
