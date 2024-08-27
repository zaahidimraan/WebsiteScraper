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
    This web scraper allows you to extract data from a website by providing the URL. \n
    You can specify the maximum depth for recursive scraping. \n
    The scraped data is displayed in a JSON format, which can be downloaded.\n
    Duplicates are removed based on the title and summary of the articles. \n
    You can download one text file of RAG String which can be used for RAG based chatbot. \n
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
        # Show processing message when scraping
        info=st.info("Scraping the website... Please wait.")
        # Perform scraping
        scraped_data = scrape_website(url, max_depth=max_depth)
        # Write scraped_data to a JSON file
        with open("scraped_data.json", "w", encoding='utf-8') as f:
            json.dump(scraped_data, f, indent=4)
        rag_string = json_to_rag_string("scraped_data.json")
        # Save rag string as txt
        with open("rag_string.txt", "w", encoding='utf-8') as f:
            f.write(rag_string)
        # Remove the processing message
        info.empty()
        # Download button
        if scraped_data:
            json_data = json.dumps(scraped_data, indent=4)  # Convert to JSON
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="scraped_data.json",
                mime="application/json",
            )
        # Display scraped data
        st.subheader("Scraped Data:")
        st.write(scraped_data)
        if rag_string:
            st.download_button(
                label="Download RAG String",
                data=rag_string,
                file_name="rag_string.txt",
                mime="text/plain",
            )
        # Display the RAG the string
        st.subheader("RAG String:")
        st.write(rag_string)

    else:
        st.warning("Please enter a valid URL.")