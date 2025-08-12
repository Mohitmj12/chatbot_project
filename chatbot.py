import pandas as pd

# Load data
try:
    df = pd.read_csv("financial_data.csv")
except Exception as e:
    print("Error reading CSV:", e)
    exit()

# Fill missing values if any
df.fillna(0, inplace=True)

# Compute growths if not present
if 'Revenue Growth (%)' not in df.columns:
    df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue'].pct_change() * 100
if 'Net Income Growth (%)' not in df.columns:
    df['Net Income Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100

df.fillna(0, inplace=True)

# Precompute summaries
summary = df.groupby('Company').agg({
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean'
}).reset_index()


def simple_chatbot(user_query):
    user_query = user_query.lower().strip()

    # Match company
    companies = ['apple', 'tesla', 'microsoft']
    company_found = next((c for c in companies if c in user_query), None)
    if not company_found:
        return "Please mention a company (Apple, Tesla, or Microsoft) in your question."

    company_cap = company_found.capitalize()
    company_data = df[df['Company'] == company_cap].sort_values('Year')
    latest = company_data.iloc[-1]

    # Revenue for specific year
    if "total revenue" in user_query and any(str(year) in user_query for year in df['Year'].unique()):
        for year in df['Year'].unique():
            if str(year) in user_query:
                value = company_data[company_data['Year'] == year]['Total Revenue'].values
                if len(value) > 0:
                    return f"{company_cap}'s total revenue in {year} was ${value[0]:,.2f}."
                else:
                    return f"No data found for {company_cap} in {year}."
    
    # Latest revenue
    elif "total revenue" in user_query:
        return f"{company_cap}'s latest total revenue is ${latest['Total Revenue']:,.2f}."

    # Net income change
    elif "net income change" in user_query or "net income changed" in user_query:
        change = company_data.iloc[-1]['Net Income'] - company_data.iloc[-2]['Net Income']
        direction = "increased" if change > 0 else "decreased"
        return f"{company_cap}'s net income has {direction} by ${abs(change):,.2f} over the last year."

    # Average revenue growth
    elif "average revenue growth" in user_query:
        avg = summary[summary['Company'] == company_cap]['Revenue Growth (%)'].values[0]
        return f"{company_cap}'s average revenue growth is {avg:.2f}%."

    # Average net income growth
    elif "average net income growth" in user_query:
        avg = summary[summary['Company'] == company_cap]['Net Income Growth (%)'].values[0]
        return f"{company_cap}'s average net income growth is {avg:.2f}%."

    # Full summary
    elif "financial summary" in user_query:
        return (
            f"{company_cap}'s latest financials:\n"
            f"- Total Revenue: ${latest['Total Revenue']:,}\n"
            f"- Net Income: ${latest['Net Income']:,}\n"
            f"- Average Revenue Growth: {summary[summary['Company'] == company_cap]['Revenue Growth (%)'].values[0]:.2f}%\n"
            f"- Average Net Income Growth: {summary[summary['Company'] == company_cap]['Net Income Growth (%)'].values[0]:.2f}%"
        )

    else:
        return "Sorry, I can only respond to predefined queries like:\n- What is the total revenue of Apple?\n- What is the average revenue growth of Tesla?\n- Tell me about Microsoft's financial summary."


# Chat loop
if __name__ == "__main__":
    print("🤖 Welcome to the Financial Chatbot!")
    print("Try asking about Apple, Tesla, or Microsoft.")
    print("Type 'exit' to quit.\n")



    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", simple_chatbot(query))
