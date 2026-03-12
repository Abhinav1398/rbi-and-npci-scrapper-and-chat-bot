from src.ingestion.pdf_parser import extract_text_from_pdf
from src.ingestion.table_extractor import extract_tables
from src.ingestion.ocr_parser import extract_text_with_ocr


def process_document(path):

    try:

        text = extract_text_from_pdf(path)

        if not text or len(text.strip()) < 50:
            print("Using OCR:", path)
            text = extract_text_with_ocr(path)

        tables = extract_tables(path)

        combined = text + "\n".join(tables)

        return combined

    except Exception as e:

        print(f"Skipping corrupted PDF: {path}")
        print(e)

        return ""