from genericpath import exists
from App import app
from App import db
from App import bcrypt
from App.models import Quote, User
from flask import jsonify, request, session
import random


@app.route('/@me', methods=['GET'])
def get_user():

    user_id = session.get('user_id')

    user = User.query.filter_by(id=user_id).first()

    if not user_id:
        return jsonify({"error": "Unauthorized XDDDDDD"}), 401

    return jsonify({
        'username': user.username,
        'email': user.email,
        'id': user.id
    })


@app.route('/', methods=['GET'])
def index():

    id_to_display = random.randint(1, 96124)
    display = Quote.query.filter_by(id=id_to_display).first()

    return jsonify({
        'quote': display.quote,
        'author': display.author,
        'category': display.category
    })


@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    email_exists = User.query.filter_by(email=email).first() is not None
    username_exists = User.query.filter_by(
        username=username).first() is not None

    if username_exists:
        return jsonify({
            'error': "username exists"
        }), 401

    if email_exists:
        return jsonify({
            'error': "email exists"
        }), 401

    password_hash = bcrypt.generate_password_hash(password)

    new_user = User(username=username, email=email, password=password_hash)

    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id

    return jsonify({
        'username': new_user.username,
        'email': new_user.email,
        'id': new_user.id
    })


@app.route('/login', methods=['POST'])
def login():
    login = request.json["login"]
    password = request.json["password"]

    exists_mail = False
    exists_username = False

    if login.find('@') > 0:
        if User.query.filter_by(email=login).first() is not None:
            exists_mail = True
    else:
        if User.query.filter_by(username=login).first() is not None:
            exists_username = True

    if exists_mail == True:
        user = User.query.filter_by(email=login).first()
    elif exists_username == True:
        user = User.query.filter_by(username=login).first()
    else:
        return jsonify({
            "error": "unauthorized"
        }), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({
            "error": "unauthorized"
            "u"
        }), 401

    session["user_id"] = user.id

    return jsonify({
        'username': user.username,
        'email': user.email,
        'id': user.id
    })
