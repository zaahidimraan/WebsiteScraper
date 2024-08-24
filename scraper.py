import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import argparse  # Import the argparse module for handling command-line arguments

def scrape_website(url, visited_urls=None, max_depth=2, current_depth=0):
    if visited_urls is None:
        visited_urls = set()
        
    # If the URL has already been visited or we've reached the max depth, stop recursion
    if url in visited_urls or current_depth > max_depth:
        return []

    print(f"Scraping URL: {url}")
    visited_urls.add(url)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Webpage retrieved successfully.")
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        print("HTML content parsed using BeautifulSoup.", soup.title)
        # Initialize a list to store the scraped data
        data = []
        
        # Find all article elements (adjust this based on the website structure)
        articles = soup.find_all()
        print(f"Found {len(articles)} elements on the webpage.")
        
        for article in articles:
            # Extract information from each article (adjust selectors as needed)
            title = article.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']).text.strip() if article.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) else 'No title'
            summary = article.find('p').text.strip() if article.find('p') else 'No summary'
            link_tag = article.find('a')
            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else 'No link'
            
            # Resolve the link to its full URL
            full_link = urljoin(url, link) if link != 'No link' else 'No link'
            
            # Create a dictionary for each article
            article_data = {
                'title': title,
                'summary': summary,
                'link': full_link
            }
            
            # Add the article data to our list
            # Duplicate data check
            # summary and link are not 'No summary' and 'No link' respectively
            if article_data['summary'] != 'No summary':
                if article_data not in data:
                    data.append(article_data)
        
        print(f"Scraped {len(data)} elements from {url}.")
        
        # Recursively follow links on the page
        for a_tag in soup.find_all('a', href=True):
            next_url = urljoin(url, a_tag['href'])
            # Ensure we only follow links within the same domain
            if urlparse(next_url).netloc == urlparse(url).netloc:
                data.extend(scrape_website(next_url, visited_urls, max_depth, current_depth + 1))
        
        return data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL of the website you want to scrape
# Set a default URL
default_url = "https://jnsedu.com/"

# Create an argument parser
parser = argparse.ArgumentParser(description="Web Scraping Project")

# Add an optional argument for the URL
parser.add_argument("--url", help="URL to scrape (overrides default)")

# Parse the arguments
args = parser.parse_args()

# Use the provided URL if given, otherwise use the default
url = args.url if args.url else default_url

# Scrape the website
scraped_data = scrape_website(url, max_depth=2)

if scraped_data:
    # Save the scraped data to a JSON file
    save_to_json(scraped_data, 'scraped_data.json')
    print("Data has been scraped and saved to scraped_data.json")
else:
    print("Failed to scrape data from the website.")
