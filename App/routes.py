from unicodedata import category
from App import app
from App import db
from App.models import Quote
from flask import jsonify
import random

@app.route('/', methods=['GET'])
def index():

    id_to_display = random.randint(1,96124)



    display = Quote.query.filter_by(id = id_to_display).first()

    return jsonify({
        'quote': display.quote,
        'author': display.author,
        'category': display.category
    })

