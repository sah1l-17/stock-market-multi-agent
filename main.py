from agents import user_agent, fetcher_agent, analyzer_agent

def run_system():
    ticker = input("Enter a stock ticker (e.g., AAPL, TSLA): ").upper()
    user_agent.send(ticker)
    fetcher_agent.run(ticker)
    analyzer_agent.run(ticker)
    print("Analysis complete. Check the saved chart.")

if __name__ == "__main__":
    run_system()
