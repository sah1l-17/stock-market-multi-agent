from agents import user_agent, fetcher_agent, analyzer_agent

def run_system():
    ticker = input("Enter a stock ticker (e.g., AAPL, TSLA): ").upper()

    # User requests stock data
    print("\n[User] Requesting stock data for:", ticker)
    stock_data = fetcher_agent.function_map["fetch_stock"](fetcher_agent, "Fetch stock data for " + ticker)
    print("[Fetcher] Response:", stock_data)

    # Analyzer agent processes stock trends
    print("\n[User] Requesting analysis for:", ticker)
    analysis_result = analyzer_agent.function_map["analyze_stock"](analyzer_agent, "Analyze stock trends for " + ticker)
    print("[Analyzer] Response:", analysis_result)

    print("\n[System] Analysis complete. Check the saved chart.")

if __name__ == "__main__":
    run_system()
