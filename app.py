from scraper import scrape_website
import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json


# Streamlit App
st.title("Web Scraper")

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

        # Download button
        if scraped_data:
            json_data = json.dumps(scraped_data, indent=4)  # Convert to JSON
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="scraped_data.json",
                mime="application/json",
            )
    else:
        st.warning("Please enter a valid URL.")