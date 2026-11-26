import json
from pathlib import Path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

OUTPUT_DIR = Path(__file__).resolve().parent
URL = "https://books.toscrape.com/"


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    results = []

    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(URL)
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

        for book in books:
            title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
            rating_element = book.find_element(By.CSS_SELECTOR, "p.star-rating")
            rating_classes = rating_element.get_attribute("class").split()
            rating = next(word for word in rating_classes if word != "star-rating")
            results.append({"Title": title, "Price": price, "Rating": rating})

    if len(results) != 20:
        raise RuntimeError(f"Expected 20 books on the homepage, found {len(results)}.")

    books_df = pd.DataFrame(results)
    print(books_df)
    books_df.to_csv(OUTPUT_DIR / "get_books.csv", index=False, encoding="utf-8")

    with (OUTPUT_DIR / "get_books.json").open("w", encoding="utf-8") as output:
        json.dump(results, output, ensure_ascii=False, indent=2)
        output.write("\n")


if __name__ == "__main__":
    main()
