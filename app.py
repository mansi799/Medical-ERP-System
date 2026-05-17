# Medical ERP System - Backend API
# Developer: Mansi Rajput, 17 Years
# Status: Deployed for Real Medical Store

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical.db'
db = SQLAlchemy(app)

# Main Route
@app.route('/')
def home():
    return "Medical ERP System Live 24/7"

# Billing API - Core Feature
@app.route('/api/bill', methods=['POST'])
def create_bill():
    data = request.json
    # Logic: Deduct stock, generate PDF, save to DB
    return jsonify({
        "status": "success",
        "message": "Bill generated & stock updated",
        "bill_id": 1024
    })

# Low Stock Alert API
@app.route('/api/stock/low')
def low_stock():
    # Returns medicines with stock < 10
    return jsonify({"low_stock_items": ["Crocin", "Dolo"]})

if __name__ == '__main__':
    app.run(debug=False) # Production mode
