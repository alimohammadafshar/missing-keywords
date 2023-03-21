import requests

# Define the URL of the webpage you want to search
url = 'https://www.example.com'

# Read the keywords from a txt file
with open('keywords.txt', 'r') as f:
    keywords = f.read().splitlines()

# Send a GET request to the URL and get the webpage content
response = requests.get(url)
content = response.text.lower()

# Find the missing keywords
missing_keywords = []
for keyword in keywords:
    if keyword.lower() not in content:
        missing_keywords.append(keyword)

# Print the missing keywords
if missing_keywords:
    print('Missing keywords:')
    for keyword in missing_keywords:
        print(keyword)
else:
    print('All keywords found!')
