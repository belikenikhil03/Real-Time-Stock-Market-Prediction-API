# database/mongo.py
from pymongo import MongoClient
import pandas as pd
from datetime import datetime

def get_mongo_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["stock_db"]
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def save_stock_data(ticker, data):
    try:
        db = get_mongo_connection()
        if db is None:
            return False
        
        collection = db["stocks"]
        
        records = []
        for _, row in data.iterrows():
            record = row.to_dict()
            record['ticker'] = ticker
            record['timestamp'] = datetime.now().isoformat()
            records.append(record)
        
        if records:
            collection.insert_many(records)
            print(f"Successfully saved {len(records)} records for {ticker}")
            return True
        return False
    except Exception as e:
        print(f"Error saving data to MongoDB: {e}")
        return False