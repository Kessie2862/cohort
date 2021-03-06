from flask import render_template, url_for
from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course")
def course():
    return render_template("course.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)