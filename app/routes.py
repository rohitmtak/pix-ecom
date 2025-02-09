from flask import Blueprint, render_template
from app.models import Product

main = Blueprint("main", __name__)

CATEGORIES = ["Bridal Couture", "Signature Collection", "Luxury Fusion Lounge", "Contemporary Drapes"]

@main.route("/")
def home():
    return render_template("home.html", categories=CATEGORIES)

@main.route("/category/<category>")
def category_products(category):
    if category not in CATEGORIES:
        return render_template("error.html", message="Category Not Found"), 404
    
    products = Product.query.filter_by(category=category).all()
    return render_template("products/category_products.html", products=products, category=category)

@main.route("/product/<slug>")
def product_detail(slug):
    product = Product.query.filter_by(slug=slug).first_or_404()
    return render_template("products/product_detail.html", product=product)
