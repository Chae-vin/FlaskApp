import os
from flask import Flask, render_template, jsonify, request
from finance import create_user, get_users, create_transaction, create_category, get_transactions
from flask_mysqldb import MySQL
from database import set_mysql
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
# Required
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
# Extra configs, optional but mandatory for this project:
app.config["MYSQL_CURSORCLASS"] = os.getenv("MYSQL_CURSORCLASS")
app.config["MYSQL_AUTOCOMMIT"] = True if os.getenv(
    "MYSQL_AUTOCOMMIT") == "true" else False

mysql = MySQL(app)
set_mysql(mysql)


@app.route("/")
def home():
    return jsonify({"message": "Hello, CSIT327!"})


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        data = request.get_json()
        user_id = create_user(
            data["username"], data["password"]
        )
        return jsonify({"id": user_id})
    else:
        users = get_users()
        return jsonify(users)


@app.route("/category", methods=["GET", "POST"])
def category():
    if request.method == "POST":
        data = request.get_json()
        cat_id = create_category(
            data["cat_name"],
        )
        return jsonify({"id": cat_id})
    else:
        category = get_category()
        return jsonify(category)


@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    if request.method == "POST":
        data = request.get_json()
        trans_id = create_transaction(
            data["user_id"], data["cat_id"],
            data["amount"], data["description"], data["trans_date"]
        )
        return jsonify({"trans_id": trans_id})
    else:
        transactions = get_transactions()
        return jsonify(transactions)
