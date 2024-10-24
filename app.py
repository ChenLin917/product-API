from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def init_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                code VARCHAR(100),
                category VARCHAR(50),
                size VARCHAR(10),
                unit_price DECIMAL(10, 2),
                inventory INT,
                color VARCHAR(50)
            )
        ''')

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

@app.route('/')
def home():
    return "Welcome to the Product API"



@app.route('/products', methods=['GET'])
def get_products():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(products)

    except mysql.connector.Error as err:
        return f"Error: {err}", 500


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        cursor.close()
        connection.close()

        if product:
            return jsonify(product)
        else:
            return "Product not found", 404

    except mysql.connector.Error as err:
        return f"Error: {err}", 500


@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        name = data.get('name')
        code = data.get('code')
        category = data.get('category')
        size = data.get('size')
        unit_price = data.get('unit_price')
        inventory = data.get('inventory')
        color = data.get('color')

        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO products (name, code, category, size, unit_price, inventory, color)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (name, code, category, size, unit_price, inventory, color))
        
        connection.commit()

        cursor.close()
        connection.close()

        return "Product added successfully!", 201

    except mysql.connector.Error as err:
        return f"Error: {err}", 500


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        name = data.get('name')
        code = data.get('code')
        category = data.get('category')
        size = data.get('size')
        unit_price = data.get('unit_price')
        inventory = data.get('inventory')
        color = data.get('color')

        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor()

        cursor.execute('''
            UPDATE products
            SET name = %s, code = %s, category = %s, size = %s, unit_price = %s, inventory = %s, color = %s
            WHERE id = %s
        ''', (name, code, category, size, unit_price, inventory, color, product_id))
        
        connection.commit()

        cursor.close()
        connection.close()

        return "Product updated successfully", 200

    except mysql.connector.Error as err:
        return f"Error: {err}", 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            database=os.getenv('MYSQL_DATABASE', 'flask_db')
        )
        cursor = connection.cursor()

        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return "Product deleted successfully", 200

    except mysql.connector.Error as err:
        return f"Error: {err}", 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
