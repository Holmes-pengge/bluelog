# -*- coding: utf-8 -*-

# @File Name:       index.py 
# @Description:    
# @Time:            2020/12/28 16:34

__author__ = 'lipeng'

from flask import Flask
from flask import jsonify
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from flask_login import current_user

from models import Product


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


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
    # result = Product.query.filter(Product.update_time < '2020-12-28 00:00:00').all()
    result = Product.query.first()
    print("==========result: ", result)
    return jsonify({'a': 10000})


# @app.route('/')
def index_2():
    return 'index_2 Hello, World!'


app.add_url_rule(rule='/index_2', endpoint='index_2', view_func=index_2)


# 开发时的程序入口
if __name__ == '__main__':
    app.run(debug=True, port=5000)
