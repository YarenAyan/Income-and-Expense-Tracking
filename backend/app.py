from flask import Flask, request, jsonify, session, redirect, url_for
from hash_util import hash_password, check_password
from financeDB_CRUD import add_income, get_incomes, update_income, delete_income, connection, cursor

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

if __name__ == "__main__":
    app.run(debug=True)