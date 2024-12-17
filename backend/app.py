from flask import Flask, request, jsonify, session, redirect, url_for
from hash_util import hash_password, check_password
from financeDB_CRUD import add_income, get_incomes, update_income, delete_income, add_expense, get_expenses, update_expense, delete_expense, connection, cursor

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Budget Tracking App!"


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if not all(key in data for key in ("username", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    username = data['username']
    email = data['email']
    password = hash_password(data['password'])
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"

    try:
        cursor.execute(query, (username, email, password))
        connection.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    if not all(key in data for key in ("username", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    username = data.get('username')
    password = data.get('password')
    query = "SELECT password FROM users WHERE username = %s"
    
    try:
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result and check_password(password, result[0].encode('utf-8')): 
            return jsonify({"message": "Login successful!"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/incomes', methods=['POST'])
def create_income():
    data = request.get_json()
    required_fields = ["amount", "category", "date", "description"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    add_income(
        amount=data['amount'],
        category=data['category'],
        date=data['date'],
        description=data['description']
    )
    return jsonify({"message": "Income added successfully!"}), 201


@app.route('/incomes', methods=['GET'])
def list_incomes():
    try:
        incomes = get_incomes() 
        return jsonify(incomes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/incomes/<int:income_id>', methods=['PUT'])
def update_income_endpoint(income_id):
    data = request.get_json()
    try:
        update_income(
            income_id=income_id,
            amount=data.get('amount', None),
            category=data.get('category', None),
            date=data.get('date', None),
            description=data.get('description', None)
        )
        return jsonify({"message": "Income updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/incomes/<int:income_id>', methods=['DELETE'])
def delete_income_endpoint(income_id):
    try:
        delete_income(income_id)  
        return jsonify({"message": "Income deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()

    required_fields = ["amount", "category", "date", "description"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        add_expense(
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data['description']
        )
        return jsonify({"message": "Expense added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/expenses', methods=['GET'])
def list_expenses():
    try:
        expenses = get_expenses() 
        return jsonify(expenses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense_endpoint(expense_id):
    data = request.get_json()

    try:
        update_expense(
            expense_id=expense_id,
            amount=data.get('amount', None),
            category=data.get('category', None),
            date=data.get('date', None),
            description=data.get('description', None)
        )
        return jsonify({"message": "Expense updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense_endpoint(expense_id):
    try:
        delete_expense(expense_id)  
        return jsonify({"message": "Expense deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)