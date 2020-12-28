# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# from bluelog.extensions import db
db = SQLAlchemy()

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True)
#
#     posts = db.relationship('Post', back_populates='category')
#
#     def search(self):
#         default_category = Product.query.get(1)
#         posts = self.posts[:]
#         for post in posts:
#             post.category = default_category
#         db.session.delete(self)
#         db.session.commit()

# item_id
# price
# seller_name
# title
# delivery_location
# url
# update_time


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
    # disabled = db.Column(db.Boolean)
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    # @staticmethod
    # def on_changed_body(target, value, oldvalue, initiator):
    #     allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
    #                     'strong']
    #     target.body_html = bleach.linkify(bleach.clean(
    #         markdown(value, output_format='html'),
    #         tags=allowed_tags, strip=True))

    # def to_json(self):
    #     json_comment = {
    #         'url': url_for('api.get_comment', id=self.id),
    #         'post_url': url_for('api.get_post', id=self.post_id),
    #         'body': self.body,
    #         'body_html': self.body_html,
    #         'timestamp': self.timestamp,
    #         'author_url': url_for('api.get_user', id=self.author_id),
    #     }
    #     return json_comment

    # @staticmethod
    # def from_json(json_comment):
    #     body = json_comment.get('body')
    #     if body is None or body == '':
    #         raise ValidationError('comment does not have a body')
    #     return Comment(body=body)

# db.event.listen(Comment.body, 'set', Comment.on_changed_body)
