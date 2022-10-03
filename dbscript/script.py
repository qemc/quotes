from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY'] = '6be575743c714c0250e548de'


db = SQLAlchemy(app)


class Quote(db.Model):

    id = db.Column(db.Integer(), primary_key=True, unique=True)
    quote = db.Column(db.Text(), nullable=False)
    author = db.Column(db.Text(), nullable=False)
    category = db.Column(db.Text())


with open(r'C:\Users\Grzegorz\Documents\Programing\quotes\dbscript\quotes_dataset.csv' , encoding='iso8859-2') as file:
    reader = csv.reader(file)

    i = 0
    for row in reader:
        for item in row:

            check1 = 'â€™'
            check2 = 'Ă'
            # if item.find(check1) > 0 or item.find(check2):
            #     break
            print(item)
            if i == 0:
                quote = item
            if i == 1:
                author = item
            if i == 2:
                category = item

                new_quote = Quote(quote=quote, author=author,
                                  category=category)
                db.session.add(new_quote)
                db.session.commit()

            i += 1
            if i > 2:
                break
        i = 0

if __name__ == '__main__':
    app.run(debug=True)
