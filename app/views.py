#路由和视图

#蓝图
from flask import Blueprint, render_template
from app.models import *

blue = Blueprint('user', __name__)

@blue.route('/')
@blue.route('/bookindex/')
def book_index():
    return render_template('book_index.html')

@blue.route('/booklist/')
def book_list():
    books =Book.query.all()

    return render_template('book_list.html', books=books)

@blue.route('/bookdetail/<int:bid>/')
def book_detail(bid):
    book=Book.query.get(bid)
    return render_template('book_detail.html', book=book)

@blue.route('/authordetail/<int:bid>/')
def author_detail(bid):
    author=Author.query.get(bid)
    return render_template('author_detail.html', author=author)

@blue.route('/publishdetail/<int:bid>/')
def publish_detail(bid):
    publish=Publisher.query.get(bid)
    return render_template('publisher_detail.html', publish=publish)