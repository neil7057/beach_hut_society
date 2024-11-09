from flask import render_template, request, flash
from beachhuts import app, db


@app.route("/")
def index():
    return render_template("index.html", page_title="Latest Forum Posts")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About B.H.A.S")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Admin")