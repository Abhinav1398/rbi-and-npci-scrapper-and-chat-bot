import httpx
from bs4 import BeautifulSoup
import os
from src.utils.logger import logger

URL = "https://rbi.org.in/scripts/ATMView.aspx"


def fetch_rbi_pdf_links():

    r = httpx.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    # find all pdf icons
    for a in soup.find_all("a", id=lambda x: x and x.startswith("APDF_")):

        href = a.get("href")

        if href and ".PDF" in href.upper():

            links.append(href)

    logger.info(f"Found {len(links)} RBI ATM PDFs")

    return links


def download_rbi_pdfs():

    os.makedirs("data/raw/rbi", exist_ok=True)

    links = fetch_rbi_pdf_links()

    for link in links:

        filename = link.split("/")[-1]

        path = f"data/raw/rbi/{filename}"

        if os.path.exists(path):
            continue

        r = httpx.get(link)

        with open(path, "wb") as f:
            f.write(r.content)

        logger.info(f"Downloaded {filename}")


if __name__ == "__main__":
    download_rbi_pdfs()