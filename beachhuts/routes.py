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
from sqlalchemy import desc, asc, or_, func
from datetime import datetime


# Home Route
@app.route("/")
def home():
    threads = list(Thread.query.order_by(desc(Thread.created_td)).all())
    # get date to calculate length of membership
    current_date = datetime.now()

    # obtain post count for current user (if logged in)
    if current_user.is_authenticated:
        user_thread_count = db.session.query(
            func.count(
                Thread.id
            )).filter(Thread.author_id == current_user.id).scalar()
    else:
        user_thread_count = None
    return render_template(
        "index.html",
        page_title="Latest Forum Posts",
        user=current_user,
        threads=threads,
        user_thread_count=user_thread_count,
        current_date=current_date
    )


@app.route("/about")
def about():
    return render_template("about.html",
    page_title="About B.H.A.S",
    user=current_user)


# Tag Routes
@app.route("/tags")
def tags():
    """
    Displaying a grid of current tags
    """
    tags = list(Tag.query.order_by(Tag.tag_name).all())
    return render_template(
        "tags.html",
        page_title="Browse by Tags",
        user=current_user,
        tags=tags)


# Add New Tag
class AddTagForm(FlaskForm):
    tag_name = StringField('Tag Name', validators=[DataRequired()])
    submit = SubmitField('Add Tag')


@app.route("/add_tag", methods=["GET", "POST"])
@login_required  # restricted to admin access only 
def add_tag():
    """
    Loads form to add a new tag
    """
    form = AddTagForm()
    if form.validate_on_submit():
        existing_tag = Tag.query.filter_by(
            tag_name=form.tag_name.data
            ).first()
        if existing_tag is None:
            tag = Tag(tag_name=form.tag_name.data)
            db.session.add(tag)
            db.session.commit()
            flash('Tag added successfully.', category='success')
            return redirect(url_for("tags"))
        else:
            flash('Tag already exists.', category='error')
    return render_template(
        "add_tag.html",
        page_title="Add a Tag",
        form=form,
        user=current_user)


# Delete Tags
@app.route("/delete_tag/<int:tag_id>")
@login_required
def delete_tag(tag_id):
    """
    restricted to Admin only by button visibility
    """
     
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    flash('Deletion Successful', category='success')
    return redirect(url_for('tags'))


# Threads  Routes
# Add a Thread
@app.route('/submit_thread', methods=['GET', 'POST'])
@login_required
def submit_thread():
    """
    Logged in Users can submit a new thread
    Users can ad existing tag caegories
    """
    if request.method == 'POST':
        thread_title = request.form.get('thread_title')
        thread_body = request.form.get('thread_body')
        selected_tag_ids = request.form.getlist('thread_tags[]')

        new_thread = Thread(
                            thread_title=thread_title,
                            thread_body=thread_body,
                            author_id=current_user.id,)

        # Add/append each tag to the thread
        for tid in selected_tag_ids:
            tag = Tag.query.get(int(tid))
            # print(tag)
            if tag:
                new_thread.tags.append(tag)

        db.session.add(new_thread)
        db.session.commit()
        flash('Your thread is now Live', category='success')
        return redirect(url_for('home'))

    tags = Tag.query.all()
    return render_template(
        "submit_thread.html",
        page_title="Create a Forum Post",
        tags=tags,
        user=current_user)


# Edit Thread
@app.route('/edit_thread/<int:thread_id>', methods=['GET', 'POST'])
@login_required
def edit_thread(thread_id):
    """
    Edit existing thread post
    """
    thread = Thread.query.get_or_404(thread_id)
    # check for author id, only author (or admin) can edit their own thread
    if current_user.id != thread.author_id and not User.site_admin:
        flash('You can only edit your own Posts.', category='error')
        return redirect(url_for('home'))

    tags = Tag.query.all()

    if request.method == 'POST':
        thread_title = request.form['thread_title']
        thread_body = request.form['thread_body']
        selected_tags_ids = request.form.getlist('thread_tags[]')
        # Update thread data
        thread.thread_title = thread_title
        thread.thread_body = thread_body
        thread.tags = [
            Tag.query.get(int(tid)) for tid in selected_tags_ids
            ]
        # commit these changes
        db.session.commit()
        flash('Forum Post updated successfully', category='success')
        return redirect(url_for('home', thread_id=thread.id))

    return render_template(
                        'edit_thread.html',
                        thread_id=thread.id,
                        page_title="Edit Forum Post",
                        thread=thread,
                        tags=tags,
                        user=current_user)


# Delete forum post (thread)
@app.route('/delete_thread/<int:thread_id>')
@login_required
def delete_thread(thread_id):
    """
    Allows users to delete their own forum posts (thread table)
    """
    thread = Thread.query.get_or_404(thread_id)
    # check for author id, only author (or admin) can delete their own thread
    if current_user.id != thread.author_id and not User.site_admin:
        flash('You can only delete your own posts.', category='error')
        return redirect(url_for('home'))
    db.session.delete(thread)
    db.session.commit()
    flash('Your Post has been successfully removed.')
    return redirect(url_for('home'))


# My Threads
@app.route('/my_threads')
def my_threads():
    """
    present current users thread posts
    """
    threads = list(Thread.query.order_by(desc(Thread.created_td)).all())
    return render_template(
        "my_threads.html",
        page_title="My Forum Posts",
        user=current_user,
        threads=threads)


# comment Route code
# add comment to a thread
@app.route('/submit_comments/<int:thread_id>', methods=['POST'])
# Only logged in users can comment on threads
@login_required
def submit_comments(thread_id):
    """
    add comment and link to thread
    be aware that table is Comments, field attribute name is comment
    """
    comment_body = request.form.get('comment_body')
    if comment_body:
        comments = Comments(
            comment_body=comment_body,
            thread_id=thread_id,
            author_id=current_user.id)

        db.session.add(comments)
        db.session.commit()
        flash('Your comment has been added to the Thread.', category='success')
    else:
        flash('Comment cannot be empty.', category='error')

    return redirect(url_for('home'))


# View Full Thread
@app.route('/view_full_thread/<int:thread_id>')
@login_required
def view_full_thread(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    return render_template(
        'view_full_thread.html',
        thread=thread,
        user=current_user)


# Search Route functionalitys
@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    """
    https://stackoverflow.com/questions/7942547/using-or-in-sqlalchemy 
    """
    search_term = request.args.get('search_term')
    if search_term:
        threads = Thread.query.join(Thread.tags).filter(
            or_(
                Thread.thread_title.ilike(f'%{search_term}%'),
                Thread.thread_body.ilike(f'%{search_term}%'),
                Tag.tag_name.ilike(f'%{search_term}%')
            )
        ).distinct().all()
    else:
        threads = []
    return render_template(
        'search_results.html',
        threads=threads,
        search_term=search_term,
        user=current_user)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template(
        "contact.html",
        page_title="Contact Admin",
        user=current_user)



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
        username = request.form.get('username')
        email_address = request.form.get('email_address').lower()
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        site_admin = False

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
                username=username,
                email_address=email_address,
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
            page_title="Sign Up",
            user=current_user
            )

@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    """
    User can amend their profile.
    """
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        username = request.form.get('username')
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        # Validate username (if it has been updated) and ensure it is unique
        user_name = User.query.filter_by(username=username).first()
        if user_name and username != user.username:
            flash(
                'Username already in use. Please choose another',
                category='error'
            )

        elif len(username) < 1:
            flash('Username required', category='error')
        elif len(fname) < 1:
            flash('First Name is required', category='error')
        elif len(lname) < 1:
            flash('Last Name is required', category='error')
        else:
            # update database fields
            user.username=username
            user.fname=fname,
            user.lname=lname,

            # update user on system
            db.session.commit()
            # Success message flash
            flash(
                'Profile Updated Successfully',
                category='success'
            )
            return redirect(url_for('home'))
    
    return render_template(
            "edit_user.html",
            user_id=user.id,
            username=user.username,
            fname=user.fname,
            lname=user.lname,
            page_title="Edit Your Profile",
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
        user = User.query.filter_by(email_address=email_address).first()
        if user:
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
        page_title="Log In",
        user=current_user)


@app.route('/logout')
# only logged in users can logout
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', category='success')
    return redirect(url_for('home'))

@app.route('/cancel')
# edit/create cancelled by user
@login_required
def cancel():
    flash('Action Cancelled by User', category='success')
    return redirect(url_for('home'))

# ADMIN ONLY Function
@app.route('/manage_users')
def manage_users():
    """
    present current users to admin for actions
    """
    users = list(User.query.order_by(asc(User.id)).all())
    return render_template(
        "manage_users.html",
        page_title="Manage Site Users",
        user=current_user,
        users=users)
