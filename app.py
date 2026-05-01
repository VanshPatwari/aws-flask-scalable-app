from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

# DB connection using environment variables
connection = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME"),
    cursorclass=pymysql.cursors.DictCursor
)

@app.route("/")
def home():
    return "CI/CD Working 🚀"

@app.route("/book", methods=["POST"])
def book():
    data = request.json

    cursor = connection.cursor()

    query = "INSERT INTO bookings (name, date) VALUES (%s, %s)"
    cursor.execute(query, (data["name"], data["date"]))

    connection.commit()

    return jsonify({"message": "Booking saved in DB"})

@app.route("/bookings", methods=["GET"])
def get_bookings():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM bookings")
    results = cursor.fetchall()

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
