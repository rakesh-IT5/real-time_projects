from flask import Flask
from config import Config
from database import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

import models

with app.app_context():
    db.create_all()
    print("Database created successfully.")
