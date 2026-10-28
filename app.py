from flask import Flask, render_template, request, jsonify
from bank import Bank

app = Flask(__name__)
bank = Bank()

@app.route("/")
def home():
    return render_template("index.html")

@app.get("/api/data")
def get_data():
    return jsonify(bank.dashboard())

@app.post("/api/create")
def create():
    try:
        return jsonify({"number": bank.create(request.json)})
    except Exception as error:
        return jsonify({"error": str(error)}), 400

@app.post("/api/action")
def action():
    try:
        data = request.json
        bank.action(data["number"], data["amount"], data["action"])
        return jsonify({"message": "Transaction successful"})
    except Exception as error:
        return jsonify({"error": str(error)}), 400

if __name__ == "__main__":
    app.run(debug=True)
