# Financial-Data-Extractor
This Streamlit application uses OpenAI's language model  to extract key financial data from news articles. Quickly identify company names, stock symbols, revenue, net income, and earnings per share (EPS) directly from your pasted text.

![Streamlit UI for Financial Data Extractor](/images/Data Extraction Tool.png)

## Features

* **User-friendly Interface:** A simple, intuitive Streamlit interface.
* **OpenAI Integration:** Leverages OpenAI's language processing capabilities.
* **Data Presentation:** Neatly formatted table for easy viewing.
* **Customizable Table:** Adjust column widths for optimal display.

## Getting Started

### Prerequisites

1. **OpenAI API Key:** Obtain an API key from OpenAI and place it in a `.env` file within this project's root directory. The file should contain:
```bash
OPENAI_API_KEY=your_api_key_here
```
2. **Dependencies:** Install the required Python packages:
```bash
pip install -r requirements.txt
```
### Usage
1. **Clone the Repository:**
```Bash
git clone [https://github.com/](https://github.com/)<your_username>/<repository_name>.git
```
2. **Run the App:**
```Bash
streamlit run main.py
```
3. **Paste Article:** Copy and paste your financial news article into the text area.

4. **Extract Data:** Click the "Extract" button.

### Code Overview
* `main.py`:
	*  Sets up the Streamlit UI (title, text area, button, results table).
	* Calls the `extract_financial_data` function from `openai_financial.py`.
	
- `openai_financial.py`:
	- Contains the core logic for interacting with the OpenAI API.
	- Takes the input text and a prompt as input.
	- Returns a Pandas DataFrame with the extracted financial data.


### Future Enhancements
- Error handling for invalid articles or API issues.
- Extraction of additional financial metrics.
- Data visualization options (charts, graphs).

### Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.
