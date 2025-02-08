from flask import Flask, render_template
from models import db, Product

app = Flask(__name__)

# List of product categories
CATEGORIES = ["Bridal Couture", "Signature Collection", "Luxury Fusion Lounge", "Contemporary Drapes"]

# Route to display products in a category
@app.route("/category/<category>")
def category_products(category):
    if category not in CATEGORIES:
        return "Category Not Found", 404
    
    products = Product.query.filter_by(category=category).all()
    return render_template("products/category_products.html", products=products, category=category)

# Route to display individual product details
@app.route("/product/<slug>")
def product_detail(slug):
    product = Product.query.filter_by(slug=slug).first_or_404()
    return render_template("products/product_detail.html", product=product)
