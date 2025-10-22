from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def start():
    return "Welcome to first page!!!"


# Sample user data
users = [
    {"id": 1, "name": "Rajesh"},
    {"id": 2, "name": "Kumar"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# GET single user by id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Build generator object for user id 
    user = (u for u in users if u["id"] == user_id) 
    # Yield first matching user id, if not present return None
    user = next(user, None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify(data), 201

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
