def remove_duplicate_articles(data):
    seen = set()
    unique_data = []

    for article in data:
        # Create a tuple of title and summary to use as a unique identifier
        identifier = (article['title'], article['summary'])
        
        if identifier not in seen:
            seen.add(identifier)
            unique_data.append(article)

    return unique_data

# Usage example
original_data = [
    {"title": "Article 1", "summary": "Summary 1", "content": "Content 1"},
    {"title": "Article 2", "summary": "Summary 2", "content": "Content 2"},
    {"title": "Article 1", "summary": "Summary 1", "content": "Content 1 (duplicate)"},
    {"title": "Article 3", "summary": "Summary 3", "content": "Content 3"},
    {"title": "Article 2", "summary": "Summary 2", "content": "Content 2 (duplicate)"}
]

deduplicated_data = remove_duplicate_articles(original_data)

print(f"Original number of articles: {len(original_data)}")
print(f"Number of articles after deduplication: {len(deduplicated_data)}")

for article in deduplicated_data:
    print(f"Title: {article['title']}, Summary: {article['summary']}")