# -*- coding: utf-8 -*-

# @File Name:       index.py 
# @Description:    
# @Time:            2020/12/28 16:34

__author__ = 'lipeng'

from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from flask_login import current_user
from datetime import datetime

db = SQLAlchemy()
# from models import Product

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lp120077@106.52.108.17:4312/lin-cms'

db.init_app(app)


class Product(db.Model):
    __tablename__ = 'product_1688'
    # id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Text)
    seller_name = db.Column(db.Text)
    title = db.Column(db.Text)
    delivery_location = db.Column(db.Text)
    url = db.Column(db.Text)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Product {}>'.format(self.__tablename__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Hello, World. \r\n' + user_agent


@app.route('/user/<name>')
def user(name):
    return "hello, {}".format(name)


# @app.route('/search/<day>')
# def search(day):
#     print("搜索近{}天的数据".format(day))
#     sql = """select * from product_1688 where update_time < '2020-12-28 00:00:00';"""
#     return jsonify({'a': 1})

@app.route('/product/<int:day>')
def show_product(day):
    print("搜索近{}天的数据".format(day))
    print(dir(Product))
    # day = request.args.get('day', 1, type=int)
    product = Product.query.filter(Product.update_time < '2020-12-28 00:00:00').first()
    # result = Product.query.first()
    print("==========result: ", product)
    item_id = product.item_id
    price = product.price
    # seller_name = db.Column(db.Text)
    # title = db.Column(db.Text)
    # delivery_location = db.Column(db.Text)
    # url = db.Column(db.Text)
    # update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    return jsonify({
        'item_id': item_id,
        'price': price,
    })


# @app.route('/')
def index_2():
    return 'index_2 Hello, World!'


app.add_url_rule(rule='/index_2', endpoint='index_2', view_func=index_2)


# 开发时的程序入口
if __name__ == '__main__':
    app.run(debug=True, port=5000)
