from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Pink Baby Dress", "price": 25, "category": "Dresses", "image": "pink-dress.jpg"},
    {"id": 2, "name": "Denim Dungarees", "price": 30, "category": "Outfits", "image": "dungarees.jpg"},
    {"id": 3, "name": "Baby Romper", "price": 20, "category": "Baby", "image": "romper.jpg"}

]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html", products=products)

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
if __name__ =="__main__":
    app.run(debug=True)
