from flask_app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    items = db.Column(db.Text)
    total = db.Column(db.Float)
