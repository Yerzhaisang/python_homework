import csv
from pathlib import Path
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://owasp.org/www-project-top-ten/"
OUTPUT_FILE = Path(__file__).resolve().with_name("owasp_top_10.csv")
RELEASE_LINK = "//a[normalize-space(.)='OWASP Top 10 2025']"
RISK_LINKS = "//main//ol[li/a[starts-with(normalize-space(.), 'A01:2025')]]/li/a"


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())

    with webdriver.Chrome(service=service, options=options) as driver:
        wait = WebDriverWait(driver, 20)
        driver.get(URL)
        release = wait.until(EC.presence_of_element_located((By.XPATH, RELEASE_LINK)))
        driver.get(release.get_attribute("href"))

        results = []
        for link in wait.until(EC.presence_of_all_elements_located((By.XPATH, RISK_LINKS))):
            results.append({"Title": link.text, "Link": link.get_attribute("href")})

    if len(results) != 10:
        raise RuntimeError(f"Expected 10 OWASP risks, found {len(results)}.")

    pprint(results, sort_dicts=False)
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=["Title", "Link"])
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()
