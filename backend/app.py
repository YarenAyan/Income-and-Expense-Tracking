from flask import Flask, request, jsonify
from hash_util import hash_password, check_password
from financeDB_CRUD import add_income, get_incomes, update_income, delete_income, connection, cursor

app = Flask(__name__)


@app.route('/register', methods=['POST'])

def register_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = hash_password(data['password'])

    query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (username, email, password))
        connection.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/login', methods=['POST'])

def login_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    query = "SELECT password_hash FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and check_password(password, result[0]):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401