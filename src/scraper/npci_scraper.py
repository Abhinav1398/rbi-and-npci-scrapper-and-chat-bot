import httpx
import os
from src.utils.logger import logger

BASE_URL = "https://www.npci.org.in"
API = "https://www.npci.org.in/api/circulars/upi"


def fetch_npci_pdfs():

    pdf_links = []

    # scrape multiple years
    years = [2025, 2024, 2023, 2022, 2021, 2020]

    for year in years:

        page = 1

        while True:

            params = {
                "pageNum": page,
                "year": year,
                "size": 10,
                "sort": "desc",
                "locale": "en"
            }

            r = httpx.get(API, params=params)

            data = r.json()

            files = data.get("data", {}).get("files", [])

            if not files:
                break

            for file in files:

                media = file.get("media")

                if media and media.get("url"):

                    url = BASE_URL + media["url"]

                    pdf_links.append(url)

                    logger.info(f"Year {year} Page {page} -> {len(files)} files")

            page += 1

    pdf_links = list(set(pdf_links))

    logger.info(f"Total NPCI PDFs found: {len(pdf_links)}")

    return pdf_links


def download_npci_pdfs():

    os.makedirs("data/raw/npci", exist_ok=True)

    links = fetch_npci_pdfs()

    for link in links:

        filename = link.split("/")[-1]

        path = f"data/raw/npci/{filename}"

        if os.path.exists(path):
            continue

        r = httpx.get(link)

        with open(path, "wb") as f:
            f.write(r.content)

        logger.info(f"Downloaded {filename}")


if __name__ == "__main__":
    download_npci_pdfs()