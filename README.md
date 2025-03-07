#Real-Time Stock Trading Engine

This project implements a simplified real-time stock trading engine that matches buy and sell orders for 1,024 tickers (stocks). It includes functionality to add orders, match orders based on price and quantity, and simulate random order submissions to mimic real-world trading activity.

##Features
Add Orders: Supports adding buy and sell orders for any of the 1,024 tickers.

Order Matching: Matches buy and sell orders based on price and quantity.

Concurrency Simulation: Simulates concurrent order submissions using threading.

Lock-Free Design: Avoids locks by using atomic operations and careful design.

Random Order Simulation: A wrapper function generates random orders to simulate active trading.

##How It Works

###Data Structures

Order Book: A list of lists, where each sublist corresponds to a ticker and contains its orders.

Order Class: Represents an order with attributes for order_type (Buy/Sell), ticker, quantity, and price.

###Functions

addOrder(order_type, ticker, quantity, price):

Adds a new order to the order book for the specified ticker.

Triggers the matchOrder function to attempt to match orders.

matchOrder(ticker):

Matches buy and sell orders for the specified ticker.

Orders are matched if the buy price is greater than or equal to the sell price.

Executes trades and updates the order book.

simulateOrders():

Simulates random order submissions in a separate thread.

Generates random order types, tickers, quantities, and prices.

Concurrency

The simulateOrders function runs in a separate thread to simulate concurrent order submissions.

The implementation avoids locks by ensuring atomic operations in the addOrder and matchOrder functions.

##How to run:
`python stocks.py`
