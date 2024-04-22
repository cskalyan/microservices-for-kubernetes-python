from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Replace with your actual product data (list of dictionaries)
products = [
    {"id": "1a", "name": "Hoodie"},
    {"id": "1b", "name": "Sticker"},
    {"id": "1c", "name": "Socks"},
    {"id": "1d", "name": "T-Shirt"},
    {"id": "1e", "name": "Beanie"},
]


@app.route("/v1/products", methods=["GET"])
def get_products():
    """
    Returns a JSON list of all products.
    """
    return jsonify(products)


@app.route("/v1/products/<string:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    """
    Returns a JSON object of a product with the given ID.
    """
    product = list(filter(lambda p: p["id"] == product_id, products))
    if not product:
        abort(404, detail="Product not found")  # Use built-in abort function for exceptions
    return jsonify(product[0])

if __name__ == "__main__":
    app.run(debug=True, port=3004)
