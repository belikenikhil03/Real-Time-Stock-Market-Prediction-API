# app.py
from flask import Flask, jsonify, render_template
from database.mongo import get_mongo_connection

app = Flask(__name__)

@app.route('/')
def index():
    return "Stock Market Prediction API is running!"

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/stocks')
def list_stocks():
    db = get_mongo_connection()
    if db is None:
        return jsonify({"error": "Database Connection Failed"}), 500
    
    collection = db["stocks"]
    # Get unique tickers
    tickers = collection.distinct("ticker")
    return jsonify({"tickers": tickers})

@app.route('/api/stocks/<ticker>/history')
def get_stock_history(ticker):
    db = get_mongo_connection()
    if db is None:
        return jsonify({"error": "Database Connection Failed"}), 500
    
    collection = db["stocks"]
    data = list(collection.find({"ticker": ticker}, 
                               {"_id": 0, "ds": 1, "y": 1, "Open": 1, "High": 1, "Low": 1, "Volume": 1})
                .sort("ds", -1).limit(30))
    
    if not data:
        return jsonify({"error": f"No data found for ticker: {ticker}"}), 404
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")