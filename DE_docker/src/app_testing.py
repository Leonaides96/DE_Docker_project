from flask import Flask, jsonify, request
from db import db
from Product import Products

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:password@db/products'
db.init_app(app)


app = Flask(__name__)

# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    products = [[product.json for product in Products.find_all()]]
    return jsonify(products)

# curl -v http://localhost:5000/products/1
@app.route('/products/<int:id>')
def get_product(id):
    # product_list = [product for product in products if product['id'] == id]
    product = Products.find_by_id(id)
    if product:
        return jsonify(product.json)
    return f'Product id not found: {id}', 404


# curl -- header "Content-Type : application/json"  --request POST --data "{}" -v http://localhost:5000/products/
@app.route('/product', methods=['POST'])
def post_product():
    print("post/product")

    request_product = request.json

    new_product = Products(None, request_product['name'])

    new_product.save_to_db()


    # Return the new product back to the client interface
    return jsonify(Products.json), 201


@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
        existing_products = Products.find_by_id(id)

        if existing_products:
            update_product = request.json

            existing_products['name'] = update_product['name']
            existing_products.save_to_db()

            return jsonify(existing_products.json), 200 
        
        return f'Product id not found for modified: {id}', 404

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    existing_products = Products.find_by_id(id)

    if existing_products:
        existing_products.delete_from_db()
        return jsonify({'message': f"Deleted product {id}"}), 200

    return f'Action abort, Product {id} is not in found in the memory', 404

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")