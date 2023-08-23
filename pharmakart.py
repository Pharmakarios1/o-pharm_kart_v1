import datetime
from flask import Flask, render_template, url_for
# from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", dt = datetime.datetime.utcnow())


@app.route("/about/")
def about():
    return render_template("about.html/")


@app.route("/featured-services/")
def services():
    return render_template("services.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/register/")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)


