# Import necessary libraries for the application
import streamlit as st             # Streamlit for creating the web app
import pandas as pd               # Pandas for data manipulation
import openai_financial           # Custom module for financial data extraction (assuming it exists)

# Create a two-column layout with a 3:2 width ratio
col1, col2 = st.columns([3, 2]) 

# Initialize an empty DataFrame to hold financial data, with default column names
financial_data_df = pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

# Content for the first (wider) column
with col1:
    # Add a title to the application
    st.title("Data Extraction Tool")

    # Create a text area for users to input financial news articles
    news_article = st.text_area("Paste your financial news article here", height=300)

    # Add a button to trigger data extraction
    if st.button("Extract"):
        # Extract financial data from the input article using the custom function
        financial_data_df = openai_financial.extract_financial_data(news_article)

# Content for the second (narrower) column
with col2:
    # Add vertical spacing to visually separate the DataFrame
    st.markdown("<br/>" * 5, unsafe_allow_html=True)  

    # Display the DataFrame containing extracted financial data with custom styling
    st.dataframe(
        financial_data_df,
        column_config={                       # Configure column widths
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True                        # Hide the index (row numbers) from the display
    ) 