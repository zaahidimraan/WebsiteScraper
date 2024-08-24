import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
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
        articles = soup.find_all('article')
        print(f"Found {len(articles)} articles on the webpage.")
        
        for article in articles:
            # Extract information from each article (adjust selectors as needed)
            title = article.find('h2').text.strip() if article.find('h2') else 'No title'
            summary = article.find('p').text.strip() if article.find('p') else 'No summary'
            link = article.find('a')['href'] if article.find('a') else 'No link'
            
            # Create a dictionary for each article
            article_data = {
                'title': title,
                'summary': summary,
                'link': link
            }
            
            # Add the article data to our list
            data.append(article_data)
        print(f"Scraped {len(data)} articles.")
        
        return data
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL of the website you want to scrape
url = "https://jnsedu.com/"  # Replace with the actual URL

# Scrape the website
scraped_data = scrape_website(url)

if scraped_data:
    # Save the scraped data to a JSON file
    save_to_json(scraped_data, 'scraped_data.json')
    print("Data has been scraped and saved to scraped_data.json")
else:
    print("Failed to scrape data from the website.")