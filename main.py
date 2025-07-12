import requests
from bs4 import BeautifulSoup
import csv

# Target website
URL = "https://books.toscrape.com/catalogue/page-1.html"

# Send HTTP request
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare CSV file
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    # Find all product containers
    products = soup.find_all("article", class_="product_pod")

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating_class = product.p["class"][1]  # e.g. 'Three'
        rating = rating_class

        # Write to CSV
        writer.writerow([name, price, rating])

print("✅ Scraping complete! Data saved in 'products.csv'")
