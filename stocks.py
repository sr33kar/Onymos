import random
import threading
import time

# Constants
NUM_TICKERS = 1024
MAX_ORDERS = 10000

# Data Structures
class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

# Global Order Book
order_book = [[] for _ in range(NUM_TICKERS)]  # List of lists for each ticker

# Add Order Function
def addOrder(order_type, ticker, quantity, price):
    if ticker < 0 or ticker >= NUM_TICKERS:
        print("Invalid ticker symbol.")
        return

    order = Order(order_type, ticker, quantity, price)
    order_book[ticker].append(order)
    print(f"Added {order_type} order for Ticker {ticker}: Quantity {quantity}, Price {price}")

    # Trigger matching
    matchOrder(ticker)

# Match Order Function
def matchOrder(ticker):
    if ticker < 0 or ticker >= NUM_TICKERS:
        print("Invalid ticker symbol.")
        return

    # Separate buy and sell orders
    buy_orders = [order for order in order_book[ticker] if order.order_type == 'Buy']
    sell_orders = [order for order in order_book[ticker] if order.order_type == 'Sell']

    # Sort buy orders in descending order of price
    buy_orders.sort(key=lambda x: -x.price)
    # Sort sell orders in ascending order of price
    sell_orders.sort(key=lambda x: x.price)

    # Match orders
    i = j = 0
    while i < len(buy_orders) and j < len(sell_orders):
        buy_order = buy_orders[i]
        sell_order = sell_orders[j]

        if buy_order.price >= sell_order.price:
            # Determine the matched quantity
            matched_quantity = min(buy_order.quantity, sell_order.quantity)

            # Execute the trade
            print(f"Matched Trade for Ticker {ticker}: "
                  f"Buy Order (Price {buy_order.price}, Quantity {matched_quantity}) "
                  f"with Sell Order (Price {sell_order.price}, Quantity {matched_quantity})")

            # Update quantities
            buy_order.quantity -= matched_quantity
            sell_order.quantity -= matched_quantity

            # Remove orders with zero quantity
            if buy_order.quantity == 0:
                order_book[ticker].remove(buy_order)
                i += 1
            if sell_order.quantity == 0:
                order_book[ticker].remove(sell_order)
                j += 1
        else:
            break  # No more matches possible

# Random Order Simulation
def simulateOrders():
    while True:
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.randint(0, NUM_TICKERS - 1)
        quantity = random.randint(1, 100)
        price = random.randint(1, 1000)
        addOrder(order_type, ticker, quantity, price)
        time.sleep(random.random())  # Simulate random delay

# Main Function
if __name__ == "__main__":
    # Start simulation in a separate thread
    simulation_thread = threading.Thread(target=simulateOrders)
    simulation_thread.daemon = True
    simulation_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped.")