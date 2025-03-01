import yfinance as yf

def fetch_stock_data(ticker):
    """
    Fetches the latest stock price for a given ticker using Yahoo Finance.
    
    :param ticker: Stock symbol (e.g., "AAPL").
    :return: Stock price or error message.
    """
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")
        
        # Check if data is empty (invalid ticker)
        if history.empty:
            return "Error: Invalid stock ticker '" + ticker + "'. Please check the symbol."

        price = history["Close"].iloc[-1]
        return "Stock: " + ticker + " | Price: $" + str(round(price, 2))
    
    except Exception as e:
        return "Error fetching stock data: " + str(e)
