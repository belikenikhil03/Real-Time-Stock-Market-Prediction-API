# Stock Prediction API

A Flask-based API for predicting Indian stock prices (BSE/NSE) using Prophet.

## Setup
1. Install Docker and Docker Compose.
2. Run `docker-compose up --build` to start Flask, MongoDB, and Redis.
3. Access API at `http://localhost:5000`.
4. Test endpoints using Postman (see `tests/postman_collection.json`).

## Endpoints
- `GET /stocks/{ticker}/history`: Fetch historical stock data (e.g., RELIANCE.NS).
- `POST /stocks/{ticker}/predict`: Predict stock prices for N days.
- `GET /dashboard`: View Plotly dashboard.

## Tech Stack
- Flask, MongoDB, Redis, Prophet, Plotly, yfinance, Docker