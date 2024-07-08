# Load environment variables (e.g., API keys)
from dotenv import load_dotenv
load_dotenv()

# Import OpenAI library for interacting with GPT models
import openai
from openai import OpenAI

# Import standard libraries for file/environment handling and data manipulation
import os
import json
import pandas as pd 

# Configure OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def extract_financial_data(text):
    """This function is to extract financial data from text using GPT-3.5-turbo

        Args:
            text (str): The input text containing a financial news article.

        Returns:
            pandas.DataFrame: A DataFrame containing the extracted financial data. 
    
       """
    prompt = get_prompt() + text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that always responds with valid JSON."},
            {"role":"user","content": prompt}]
    )
    output_content = response.choices[0].message.content
    try:
        data = json.loads(output_content)
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])
        df = df.reset_index() 
        df = df.rename(columns={'index': 'Measure'}) 
    except (json.JSONDecodeError, IndexError):
        df = pd.DataFrame({
            "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
            "Value": ["", "", "", "", ""]})
    return df


# Helper function to load the prompt template
def get_prompt():
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }'''


if __name__ == '__main__':    
    text = '''
    Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $
    '''
    df = extract_financial_data(text)
    print(df)
