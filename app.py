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
    items = data.get("items")
    total = data.get("total")

    # Save to database
    new_order = Order(items=str(items), total=total)
    db.session.add(new_order)
    db.session.commit()

    # Simulated email receipt
    print("\n--- Simulated Email Receipt ---")
    print("To: customer@example.com")
    print("Subject: Your Sweetleaf & Co. Order Receipt")
    print("Items Ordered:")
    for item in items:
        print(f" - {item['name']} - ${item['price']:.2f}")
    print(f"Total: ${total:.2f}")
    print("-------------------------------\n")

    return jsonify({"message": "Order received and receipt simulated."}), 201


application = app
