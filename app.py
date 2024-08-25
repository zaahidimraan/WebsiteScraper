from scraper import scrape_website
from ragstringmaker import json_to_rag_string
import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json


# Streamlit App
st.title("Web Scraper")

# Web Scraper Features
st.markdown(
    """
    This web scraper allows you to extract data from a website by providing the URL. 
    You can specify the maximum depth for recursive scraping. 
    The scraped data is displayed in a JSON format, which can be downloaded.
    Duplicates are removed based on the title and summary of the articles.
    You can download one text file of RAG String which can be used for RAG based chatbot.
    """
)

# URL input
url = st.text_input("Enter the website URL to scrape:")

# Max depth input
max_depth = st.number_input("Enter the maximum depth for recursive scraping:", min_value=0, value=2)

# Scrape button
if st.button("Scrape"):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Perform scraping
        scraped_data = scrape_website(url, max_depth=max_depth)

        # Display scraped data
        st.subheader("Scraped Data:")
        st.write(scraped_data)
        
        # Display the RAG the string
        rag_string = json_to_rag_string("scraped_data.json")
        st.subheader("RAG String:")
        st.write(rag_string)

        # Download button
        if scraped_data:
            json_data = json.dumps(scraped_data, indent=4)  # Convert to JSON
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="scraped_data.json",
                mime="application/json",
            )
        if rag_string:
            st.download_button(
                label="Download RAG String",
                data=rag_string,
                file_name="rag_string.txt",
                mime="text/plain",
            )
    else:
        st.warning("Please enter a valid URL.")