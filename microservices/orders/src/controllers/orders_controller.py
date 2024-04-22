from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException
import requests  # Replace with appropriate HTTP library if not using requests

app = Flask(__name__)

# Array of orders (assuming basic structure)
orders = [
    {"id": "1", "productId": "1a", "orderFor": "Herbert Kelvin Jr.", "deliveryAddress": "Asphalt Street", "deliveryDate": "02/11/2023", "deliveryType": "STANDARD"},
    {"id": "2", "productId": "1b", "orderFor": "John Zulu Nunez", "deliveryAddress": "Beta Road", "deliveryDate": "10/10/2023", "deliveryType": "FAST DELIVERY"},
    {"id": "3", "productId": "1c", "orderFor": "Lael Fanklin", "deliveryAddress": "Charlie Avenue", "deliveryDate": "02/10/2023", "deliveryType": "STANDARD"},
    {"id": "4", "productId": "1d", "orderFor": "Candice Chipilli", "deliveryAddress": "Delta Downing Street", "deliveryDate": "02/19/2023", "deliveryType": "FAST DELIVERY"},
    {"id": "4", "productId": "1e", "orderFor": "Tedashii Tembo", "deliveryAddress": "Echo Avenue", "deliveryDate": "12/12/2023", "deliveryType": "FAST DELIVERY"}
    # ... other orders (same format)
    
]


@app.route("/v1/orders", methods=["GET"])
def get_orders():
    """
    Fetches all orders
    """
    return jsonify(orders)


@app.route("/v1/orders/products", methods=["GET"])
async def get_orders_with_products():
    """
    Fetches orders with their associated products
    """
    try:
        orders_with_products = []
        for order in orders:
            product_url = f"http://{app.config['PRODUCTS_SERVICE_HOST']}/v1/products/{order['productId']}"
            response = requests.get(product_url)
            if response.status_code == 200:
                product = response.json()
                orders_with_products.append({**order, "product": product})
            else:
                # Handle product service errors (e.g., log, return specific error)
                print(f"Error fetching product {order['productId']}: {response.status_code}")
                return abort(500, detail="Error fetching product data")

        return jsonify(orders_with_products)

    except Exception as e:
        # Handle generic errors
        print(f"Error retrieving orders or products: {e}")
        return abort(500, detail="Internal server error")


# Configuration for product service connection (replace with actual values)
app.config['PRODUCTS_SERVICE_HOST'] = "localhost:3004"

if __name__ == "__main__":
    app.run(debug=True, port=3003)
