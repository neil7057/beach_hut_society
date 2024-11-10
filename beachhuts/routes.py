from flask import render_template, request, flash, redirect, url_for, jsonify
from beachhuts import app, db
from beachhuts.models import User, Thread, Comments, Tag

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from flask_login import current_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Sort threads by date using SQLAlchemy desc to present most recent first
from sqlalchemy import desc, or_, func
from datetime import datetime

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