import os

from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')


products = [
    {
        "id": 1,
        "name": "Pink Baby Dress",
        "price": 25,
        "category": "Dresses",
        "image": "pink-dress.jpg"
    },
    {
        "id": 2,
        "name": "Denim Dungarees",
        "price": 30,
        "category": "Outfits",
        "image": "dungarees.jpg"
    },
    {
        "id": 3,
        "name": "Baby Romper",
        "price": 20,
        "category": "Baby",
        "image": "romper.jpg"
    }
]


@app.route("/")
def home():
    featured = products[:3]
    return render_template("index.html", featured=featured)


@app.route("/shop")
def shop():
    return render_template("shop.html", products=products)


@app.route("/product")
def product():
    product = {
        "name": "Pink Floral Dress",
        "price": 25,
        "category": "Girls",
        "description": "A cute and comfortable floral dress for little ones."
    }

    return render_template("product.html", product=product)

@app.route("/about")
def about():
    return render_template("about.html")

# when you visit /contact, the browser makes a GET request, so Flask displays your contact page. And when you click Send Message, the form makes a POST request
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        return f"Thank you, {name}! We have received your message."

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    