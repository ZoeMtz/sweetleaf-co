from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "sweetleaf.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(255))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Text)
    total = db.Column(db.Float)
    email = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id, "name": p.name, "price": p.price, "image_url": p.image_url
    } for p in products])

@app.route("/api/orders", methods=["POST"])
def place_order():
    data = request.get_json()
    new_order = Order(
        items=str(data.get("items")),
        total=data.get("total"),
        email=data.get("email")
    )
    db.session.add(new_order)
    db.session.commit()
    print("Simulated email sent to:", data.get("email"))
    return jsonify({"message": "Order received"}), 201

application = app
