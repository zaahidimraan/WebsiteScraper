import json

def json_to_rag_string(json_file_path):
    # Try different encodings
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(json_file_path, 'r', encoding=encoding) as file:
                data = json.load(file)
            break  # If successful, break out of the loop
        except UnicodeDecodeError:
            continue  # If unsuccessful, try the next encoding
        except json.JSONDecodeError:
            print(f"File is not valid JSON. Please check the file content.")
            return ""
    else:
        # If no encoding worked
        print(f"Unable to decode the file with any of the attempted encodings: {encodings}")
        return ""

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each article in the data
    for article in data:
        # Add title if it's not 'No title'
        if article.get('title', 'No title') != 'No title':
            result += f"{article['title']}. "

        # Add summary if it's not 'No summary'
        if article.get('summary', 'No summary') != 'No summary':
            result += f"{article['summary']}. "
        # Add an extra space between articles for clarity
        result += " "

    return result.strip()  # Remove trailing whitespace

if __name__ == "__main__":
    # Usage example
    json_file_path = "scraped_data.json"
    rag_string = json_to_rag_string(json_file_path)

    if rag_string:
        print("RAG String Preview:")
        print(rag_string[:500] + "..." if len(rag_string) > 500 else rag_string)
        print(f"\nTotal characters: {len(rag_string)}")
        # Save the RAG string to a text file
        with open("rag_string.txt", 'w', encoding='utf-8') as file:
            file.write(rag_string)
    else:
        print("Failed to process the JSON file.")