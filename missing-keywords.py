import requests

# Define the URL of the webpage you want to search
url = 'https://www.example.com'

# Read the keywords from a txt file
with open('keywords.txt', 'r') as f:
    keywords = f.read().split()

# Send a GET request to the URL and get the webpage content
response = requests.get(url)
content = response.text

# Create a set of all words in the content
content_words = set(content.split())

# Create a set of all words in the keywords.txt file
keyword_words = set(keywords)

# Find the words that are in keywords.txt but not in the content
missing_words = keyword_words - content_words

# Print the missing words
if missing_words:
    print('Missing words:')
    for word in missing_words:
        print(word)
else:
    print('All words found!')
