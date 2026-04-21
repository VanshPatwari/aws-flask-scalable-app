from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# DB connection
connection = pymysql.connect(
    host="YOUR_RDS_ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD",
    database="clinic"
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