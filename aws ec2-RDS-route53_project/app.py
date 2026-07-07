from flask import Flask, render_template, request
from config import Config
from database import db
from models import User

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    user = User(
        name=name,
        email=email,
        phone=phone
    )

    db.session.add(user)
    db.session.commit()

    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
