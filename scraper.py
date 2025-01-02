from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv


service = Service(r"CHROME DRIVER PATH")  # Replace with your actual path
driver = webdriver.Chrome(service=service)

# URL to scrape
url = "http://books.toscrape.com"

try:
    
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all books (titles and prices)
    books = soup.find_all('article', class_='product_pod')

    # Collect data
    data = []
    for book in books:
        title = book.h3.a['title']  # Get book title
        price = book.find('p', class_='price_color').text  # Get book price
        data.append((title, price))

    # Save to CSV
    with open("books_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Price"])  # Write headers
        writer.writerows(data)  # Write data rows

    print("Data saved to 'books_data.csv'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
