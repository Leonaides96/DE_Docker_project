from flask import Flask, jsonify, request

products = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"}
]

app = Flask(__name__)

# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products)

# curl -v http://localhost:5000/products/1
@app.route('/products/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Product id not found: {id}', 404
    
    return jsonify(product_list[0])

# curl -- header "Content-Type : application/json"  --request POST --data "{}" -v http://localhost:5000/products/
@app.route('/product', methods=['POST'])
def post_product():
    # Retrieve the product from the request body
    request_product = request.json 

    # Generate an ID for the new post
    new_id = max([product['id'] for product in products]) + 1 # Leo - the id generator is not quite well

    # Creata a new product
    new_product = {
        "id": new_id,
        "name": request_product['name']
    }

    # append the new product to the existing linst
    products.append(new_product)

    # Return the new product back to the client interface
    return jsonify(new_product), 201


@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    # Retrieve the updated product information
    updated_product = request.json 

    # Find the production
    for product in products:
        if product['id'] == id:
            product['name'] = updated_product['name']
            return jsonify(product), 200 
        
    return f'Product id not found for modified: {id}', 404

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    
    # Detect the id to be deleted
    deleted_product = [product for product in products if product['id']== id]

    # Removing the produclt
    if len(deleted_product) ==1:
        products.remove(deleted_product)
        return f'Product {id} have been removed from the memory', 200
    
    return f'Action abort, Product {id} is not in found in the memory', 404

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")