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



@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    """
    Routing for sign up process.
    """
    if current_user.is_authenticated:
        # If the user is already logged in, redirect to the home page
        flash('You are already logged in.', category='error')
        return redirect(url_for('home'))

    if request.method == 'POST':
        email_address = request.form.get('email_address').lower()
        username = request.form.get('username')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        site_admin = True
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Validate user email and ensure it is unique
        user = User.query.filter_by(email_address=email_address).first()
        if user:
            flash(
                'This Email is already registered. Login or use another to Sign up.',
                category='error'
            )

        # Validate username and ensure it is unique
        user_name = User.query.filter_by(username=username).first()
        if user_name:
            flash(
                'Username already in use. Please choose another',
                category='error'
            )
        if len(username) < 1:
            flash('Username required', category='error')
        elif len(fname) < 1:
            flash('First Name is required', category='error')
        elif len(lname) < 1:
            flash('Last Name is required', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 8:
            flash(
                'Password must be at least 8 characters',
                category='error'
            )
        else:
            # add new user to database
            new_user = User(
                email_address=email_address,
                username=username,
                fname=fname,
                lname=lname,
                site_admin=site_admin,
                password=generate_password_hash(
                    request.form.get("password1")
                )
            )
            # add user to system
            db.session.add(new_user)
            db.session.commit()
            # Success message flash
            flash(
                'Account Created! Please login',
                category='success'
            )
            return redirect(url_for('login'))
    
    return render_template(
            "sign_up.html",
            page_title="Sign Up!",
            user=current_user
            )


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Present login page 
    """
    if request.method == 'POST':
        email_address = request.form.get('loginEmail').lower()
        password = request.form.get('password')
        remember_me = 'remember_me' in request.form
        print(f"Attempting login with email: {email_address}")
        user = User.query.filter_by(email_address=email_address).first()
        if user:
            print(f"User found: {user.email_address}")  # Debug print
            if check_password_hash(user.password, password):
                flash('You are Logged In!', category='success')
                if remember_me:
                    login_user(user, remember=True)
                else:
                    login_user(user, remember=False)
                return redirect(url_for('home'))
            else:
                flash(
                    'Incorrect password - please try again!',
                    category='error'
                )
        else:
            flash(
                'Invalid login - email not registered',
                category='error'
            )

    return render_template(
        "login.html",
        page_title="Log In!",
        user=current_user)


@app.route('/logout')
# only logged in users can logout
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', category='success')
    return redirect(url_for('home'))