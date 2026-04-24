import requests
from bs4 import BeautifulSoup

def scrape_books(pages=2):
    data = []

    for page in range(1, pages + 1):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.find_all("article", class_="product_pod")

        for item in items:
            data.append(item)

    return data