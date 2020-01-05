from datetime import datetime
from Francis import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Column


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String())
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    ciclo = db.Column(db.String())
    anno = db.Column(db.String())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='2e32b4c96a8d8f10.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Post('{self.title}', '{self.date_posted}')"
