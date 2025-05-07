from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

# ======= Configurations =======
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweetleaf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '8c585d002@smtp-brevo.com'
app.config['MAIL_PASSWORD'] = '1mARIb6KFnj4HaUE'
mail = Mail(app)

db = SQLAlchemy(app)

# ======= Models =======
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    customer_email = db.Column(db.String(100))
    total = db.Column(db.Float)

# ======= Routes =======

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/checkout2")
def checkout2():
    total = 12.97
    return render_template("checkout2.html", total=total)

@app.route("/submit_order", methods=["POST"])
def submit_order():
    name = request.form.get("name")
    email = request.form.get("email")
    total = request.form.get("total")

    order = Order(customer_name=name, customer_email=email, total=total)
    db.session.add(order)
    db.session.commit()

    # Skip email due to PythonAnywhere free-tier restrictions
    # msg = Message(
    #     "Sweetleaf Order Confirmation",
    #     sender=app.config['MAIL_USERNAME'],
    #     recipients=[email]
    # )
    # msg.body = f"Hi {name},\\n\\nThank you for your order of ${total} from Sweetleaf & Co!"
    # mail.send(msg)

    return redirect(url_for("order_confirmed"))

@app.route("/order_confirmed")
def order_confirmed():
    return render_template("order_confirmed.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/customer_login")
def customer_login():
    return render_template("customer_login.html")

# ======= Product Pages =======

@app.route("/product_chamomile")
def product_chamomile():
    return render_template("show_product_2.html")

@app.route("/product_mint")
def product_mint():
    return render_template("show_product_1.html")

@app.route("/product_earl_grey")
def product_earl_grey():
    return render_template("show_product_3.html")

@app.route("/product_hibiscus")
def product_hibiscus():
    return render_template("show_product_4.html")

# ======= Admin =======

@app.route("/admin_index")
def admin_index():
    return render_template("admin_index.html")

@app.route("/admin_orders")
def admin_orders():
    orders = Order.query.all()
    return render_template("admin_orders.html", orders=orders)

@app.route("/admin_product")
def admin_product():
    return render_template("admin_product.html")

# ======= API =======

@app.route("/api/items")
def get_items():
    items = Product.query.all()
    return jsonify([item.to_dict() for item in items])

# ======= Run =======

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
