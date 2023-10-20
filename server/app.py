from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "hey there"
@app.route("/calculate/tax", methods=["POST"])
def calculatetax():
    try:
        data = request.get_json()
        
        income = int(data["income"])
        
        if income <= 300000:
            tax = 0
        elif income <= 600000:
            tax = (300000 / 100) * 5
        elif income <= 900000:
            tax = (300000 / 100) * 5 + ((income - 600000) / 100) * 10
        elif income <= 1200000:
            tax = (300000 / 100) * 5 + (300000 / 100) * 10 + ((income - 900000) / 100) * 15
        elif income <= 1500000:
            tax = (300000 / 100) * 5 + (300000 / 100) * 10 + (300000 / 100) * 15 + ((income - 1200000) / 100) * 20
        else:
            tax = (300000 / 100) * 5 + (300000 / 100) * 10 + (300000 / 100) * 15 + (300000 / 100) * 20 + ((income - 1500000) / 100) * 30

        cess = (tax / 100) * 4
        taxvalue = tax + cess

        formatted_taxvalue = "{:.2f}".format(taxvalue)

        return jsonify({"taxvalue": formatted_taxvalue})
    
    except Exception as e:
        return jsonify({"error": str(e)})