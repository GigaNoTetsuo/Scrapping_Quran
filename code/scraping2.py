import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://corpus.quran.com/topics.jsp"

# Send a GET request to the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main content div
content_div = soup.find('div', class_='content')

# Extract all <a> tags inside <p> tags within the content div
results = []
for p_tag in content_div.find_all('p'):
    a_tag = p_tag.find('a')
    if a_tag:
        text = a_tag.get_text(strip=True)
        href = a_tag.get('href')
        results.append({'text': text, 'url': f"https://corpus.quran.com{href}"})

# Print or save the results
for item in results:
    print(item)
