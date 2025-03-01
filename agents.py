from autogen import AssistantAgent, UserProxyAgent
from tools import fetch_stock_data

# Define agents
fetcher_agent = AssistantAgent(name="StockFetcher", system_message="Fetches stock prices and trends.")
analyzer_agent = AssistantAgent(name="StockAnalyzer", system_message="Analyzes stock trends and gives insights.")
user_agent = UserProxyAgent(name="UserAgent", code_execution_config={"use_docker": False})

# Define agent workflows
def fetch_stock(agent, message):
    ticker = message.split()[-1]  # Extract ticker from message
    result = fetch_stock_data(ticker)
    return result  # Return stock data

def analyze_stock(agent, message):
    ticker = message.split()[-1]
    response = "Analyzing trends for " + ticker + "... Fetching insights..."
    return response

# Register functions correctly
fetcher_agent.register_function({"fetch_stock": fetch_stock})
analyzer_agent.register_function({"analyze_stock": analyze_stock})

import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="7d")  # Fetch last 7 days of data
        
        if history.empty:
            return "No stock data found for " + ticker
        
        price = history["Close"].iloc[-1]

        # Save chart
        plt.figure(figsize=(8, 4))
        plt.plot(history.index, history["Close"], marker="o", linestyle="-", color="blue")
        plt.title("Stock Price for " + ticker)
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.grid(True)
        chart_path = ticker + "_stock_chart.png"
        plt.savefig(chart_path)  # Save the chart as an image
        plt.close()

        return "Stock: " + ticker + " | Price: $" + str(round(price, 2)) + " (Chart saved as " + chart_path + ")"

    except Exception as e:
        return "Error fetching stock data: " + str(e)