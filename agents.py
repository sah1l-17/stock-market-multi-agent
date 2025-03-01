from autogen import AssistantAgent, UserProxyAgent
from tools import fetch_stock_data

# Define agents
fetcher_agent = AssistantAgent(name="StockFetcher", system_message="Fetches stock prices and trends.")
analyzer_agent = AssistantAgent(name="StockAnalyzer", system_message="Analyzes stock trends and gives insights.")
user_agent = UserProxyAgent(name="UserAgent", code_execution_config={"use_docker": False})

# Define agent workflows
def fetch_stock(agent, ticker):
    result = fetch_stock_data(ticker)
    agent.send(result)

def analyze_stock(agent, ticker):
    response = f"Analyzing trends for {ticker}. Fetching insights..."
    agent.send(response)

# Link agents
user_agent.initiate_chat(fetcher_agent, message="Get stock data for AAPL")
fetcher_agent.register_function(fetch_stock)
analyzer_agent.register_function(analyze_stock)