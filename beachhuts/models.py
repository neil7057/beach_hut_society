from beachhuts import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    # schema for the User Model
    """
    UserMixin supporst Flask_login for authentication checkimg.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email_address = db.Column(db.String(100))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    password = db.Column(db.String(255))
    site_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_td = db.Column(db.DateTime(timezone=True), default=func.now())



class Thread(db.Model):
    # schema for the Thread model
    id = db.Column(db.Integer, primary_key=True)
    thread_title = db.Column(db.String(50), unique=True, nullable=False)
    thread_body = db.Column(db.Text, nullable=False)
    tags = db.relationship(
                            'Tag',
                            secondary=thread_tag_link,
                            lazy='subquery',
                            backref=db.backref('threads', lazy=True)
                            )
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)
    created_td = db.Column(db.DateTime(timezone=True), default=func.now())

    # relationship
    author = db.relationship('User', backref='threads')

    def __repr__(self):
        return "Thread #{0} - Title: {1} | Urgent: {2}".format(
            self.id, self.thread_title, self.author_id
        )


# Add comments model
class Comments(db.Model):
    """
    Threads can have replies - termed comments attached
    There may be multiple comments from potentially multiple users
    """
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text, nullable=False)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)
    thread_id = db.Column(
        db.Integer,
        db.ForeignKey('thread.id'),
        nullable=False)
    created_td = db.Column(db.DateTime(timezone=True), default=func.now())

    # Relationships
    author = db.relationship('User', backref='posts')
    question = db.relationship('Thread', backref=db.backref(
        'posts',
        lazy=True,
        cascade="all, delete-orphan"
        ))

    def __repr__(self):
        return (
            f'Comment #{self.id} by User ID {self.author_id} '
            f'on Thread ID {self.thread_id}'
        )


class Tag(db.Model):
    # schema for the Tag model
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        # __repr___ to represent itself in the form of a string
        return self.tag_name  


# Intermediate table to implement M:M relationship
Thread_tag_link = db.Table(
    'links a tag to a thread',
    db.Column(
        'thread_id',
        db.Integer,
        db.ForeignKey('thread.id'),
        primary_key=True
        ),
    db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey('tag.id'),
        primary_key=True
        )
)

