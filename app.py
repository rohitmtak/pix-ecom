from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/collection/bridal-couture")
def bridalCouture():
    return render_template("products/bridal_couture.html")


if __name__ == "__main__":
    app.run(debug=True)