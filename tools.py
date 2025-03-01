import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "3mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)

    if hist.empty:
        return "Invalid stock ticker or no data available."

    # Calculate moving averages
    hist["SMA_20"] = hist["Close"].rolling(window=20).mean()
    hist["SMA_50"] = hist["Close"].rolling(window=50).mean()

    # Plot stock prices
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist["Close"], label="Closing Price", color="blue")
    plt.plot(hist.index, hist["SMA_20"], label="20-day SMA", linestyle="dashed", color="green")
    plt.plot(hist.index, hist["SMA_50"], label="50-day SMA", linestyle="dashed", color="red")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Price & Trend Analysis")
    plt.legend()
    plt.grid()
    plt.savefig(f"{ticker}_chart.png")  # Save chart for sharing
    plt.close()

    return f"Stock analysis complete for {ticker}. Trends plotted."
