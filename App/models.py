from App import db

class Quote(db.Model):

    id = db.Column(db.Integer(), primary_key=True, unique=True)
    quote = db.Column(db.Text(), nullable=False)
    author = db.Column(db.Text(), nullable=False)
    category = db.Column(db.Text())
