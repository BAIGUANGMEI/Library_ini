#创建Flask应用
from flask import Flask, render_template, request, redirect, url_for, flash, session
from .views import blue
from .exts import init_ext
def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(blueprint=blue)

    #初始化配置数据库
    #db_uri = 'sqlite:///db.sqlite3.db'
    #mysql
    db_uri = 'mysql+pymysql://root:mzh553214@localhost:3306/bookdatabase'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_ext(app)

    return app
