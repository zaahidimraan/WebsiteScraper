import requests
from bs4 import BeautifulSoup
import json

def analyze_structure(url):
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, 'html.parser')
    
    structure = {
        "title": soup.title.string if soup.title else "No title found",
        "meta_description": soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else "No meta description found",
        "h1_tags": [h1.text for h1 in soup.find_all('h1')],
        "main_content_candidates": []
    }

    # Look for potential main content containers
    main_tags = soup.find_all(['main', 'article', 'div', 'section'])
    for tag in main_tags:
        if tag.get('id') or tag.get('class'):
            structure["main_content_candidates"].append({
                "tag": tag.name,
                "id": tag.get('id'),
                "classes": tag.get('class'),
                "text_snippet": tag.text[:100] + "..." if len(tag.text) > 100 else tag.text
            })

    return json.dumps(structure, indent=2)

# Usage
url = "https://jnsedu.com/"  # Replace with the URL you want to analyze
print(analyze_structure(url))