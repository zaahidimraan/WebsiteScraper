# Web Scraping Project
You can interact with Scraper: [Link](https://websitescraper.streamlit.app/)

This project focuses on extracting data from website using Python's `requests` library for fetching web pages and `BeautifulSoup` for parsing HTML content. 

# Features
    This web scraper allows you to extract data from a website by providing the URL. 
    You can specify the maximum depth for recursive scraping. 
    The scraped data is displayed in a JSON format, which can be downloaded.
    Duplicates are removed based on the title and summary of the articles. 
    You can download one text file of RAG String which can be used for RAG based chatbot. 

## Project Structure

* `scraper.py`:  Main Python script containing the web scraping logic.
* `app.py` : Streamlit app to make the UI for easy access
* `requirements.txt`:  Lists the project dependencies.
* `README.md`:  This file providing an overview of the project.
