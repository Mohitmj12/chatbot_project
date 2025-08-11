# Rule-Based Financial Chatbot (Prototype)

## 🔍 Project Context
This chatbot prototype is developed as part of GFC’s initiative with BCG Tech Hub to improve accessibility of complex financial insights. The chatbot uses rule-based logic to answer predefined financial queries about major corporations like Apple, Tesla, and Microsoft based on 10-K data analysis.

## 👨‍💻 Your Role
As part of a cross-functional team, my focus was on **implementing the rule-based logic**. This means designing a system that can accurately respond to a fixed set of financial questions using hardcoded logic and extracted data. Other team roles include:
- **NLP Experts** – Enhance conversational capabilities.
- **ML Engineers** – Add learning-based adaptability.
- **UX Designers** – Improve interface and usability.
- **Data Integration Specialists** – Ensure real-time financial data access.

## 💬 Predefined Queries Supported
- What is the total revenue?
- How has net income changed over the last year?
- What is the average revenue growth rate?
- What is the net income growth trend?
- Compare revenue of Apple and Tesla.

## 🧠 Chatbot Logic
Implemented using simple `if-else` rules in Python:

```python
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "Apple's total revenue in 2023 was $394.3 billion."
    elif user_query == "How has net income changed over the last year?":
        return "Apple's net income decreased by 5% in 2023."
    else:
        return "Sorry, I can only answer predefined questions."
