# Stock Market Multi-Agent System

## 📌 Overview
This project is a **multi-agent system** designed to fetch and analyze stock market data using `yfinance`. It utilizes the **AutoGen agentic framework** to create an interactive, intelligent stock market assistant.

### **🚀 Features**
✅ Fetch real-time stock price data using `yfinance`  
✅ Compute **Moving Averages (SMA-20 & SMA-50)** for trend analysis  
✅ Generate **visual charts** for stock performance  
✅ Implement a **multi-agent system** using AutoGen  
✅ Modular & extensible architecture for future enhancements  

---

## 📁 Project Structure
```
finance_agent/
├── main.py  # Entry point
├── agents.py  # Agent definitions
├── tools.py  # Stock data fetching & analysis
├── requirements.txt  # Dependencies
├── README.md  # Documentation
```

---

## ⚙️ Setup & Installation
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the System**
```bash
python main.py
```

---

## 🛠️ How It Works
### **🔹 Agents**
- **StockFetcher Agent** → Fetches stock data from `yfinance`  
- **StockAnalyzer Agent** → Analyzes stock trends & moving averages  
- **UserAgent** → Manages user interaction  

### **🔹 Workflow**
1. User inputs a **stock ticker** (e.g., `AAPL`)
2. The **StockFetcher Agent** retrieves historical price data
3. The **StockAnalyzer Agent** computes **SMA trends** and generates a **visual chart**
4. The user receives a **detailed stock analysis & graph**

---

## 🖥️ Example Output
```plaintext
Enter a stock ticker (e.g., AAPL, TSLA): AAPL
Fetching stock data...
Stock analysis complete for AAPL. Check the saved chart.
```
The system saves and displays a **trend analysis chart** for the stock.

---

## 📊 Visualization Example
When you enter `AAPL`, the system generates a **trend chart** like this:
![Example Chart](AAPL_chart.png)

---

## 🔥 Future Enhancements
- ✅ **Streamlit UI** for an interactive web interface
- ✅ **Sentiment Analysis** using news headlines
- ✅ **Multi-stock comparison**

---

## 👨‍💻 Contributing
Feel free to fork the repo, suggest improvements, or add new features!

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📞 Contact
For queries, reach out at **sahil069917@gmail.com**

