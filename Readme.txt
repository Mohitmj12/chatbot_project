📘 Financial Chatbot Prototype

This is a simple rule-based chatbot that answers basic financial queries based on analyzed 10-K data from Apple.

✅ Predefined queries:
1. What is the total revenue?
2. How has net income changed over the last year?
3. What is the average revenue growth?
4. What is the average net income growth?
5. Tell me about Apple’s financial summary.

🔧 How it works:
- The chatbot loads an Excel file containing financial data.
- It computes year-over-year revenue and net income growth.
- Based on user input, it returns pre-written responses using the latest or average metrics.

⚠️ Limitations:
- Only answers 5 specific queries.
- Works only for Apple (you can expand to Tesla/Microsoft easily).
- Does not use NLP — exact wording is required.

📂 Files:
- chatbot.py: Python script for chatbot
- financial_data.xlsx: Contains the structured financial data
- README.txt: This file

👨‍💻 To run:
Make sure Python and pandas are installed. Open a terminal and run:
> python chatbot.py
