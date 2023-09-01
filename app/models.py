# 数据库
from .exts import db


# 创建模型类
class Author(db.Model):
    # 表名
    __tablename__ = 'author'
    # 字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer, default=18)
    sex =db.Column(db.Boolean, default=True)
    email = db.Column(db.String(50))

    books =db.relationship('Book', backref='author', lazy='dynamic')

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title= db.Column(db.String(30))
    date =db.Column(db.Date)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

book_pubisher = db.Table('book_publisher',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'), primary_key=True)
)

class Publisher(db.Model):
    __tablename__ = 'publisher'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    province = db.Column(db.String(50))
    country = db.Column(db.String(50))
    website = db.Column(db.String(200))

    books = db.relationship('Book', secondary=book_pubisher, backref='publishers', lazy='dynamic')

