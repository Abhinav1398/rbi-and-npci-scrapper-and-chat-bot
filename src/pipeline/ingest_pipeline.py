import os

from src.ingestion.document_processor import process_document
from src.ingestion.chunker import chunk_text
from src.ingestion.embedder import generate_embeddings
from src.ingestion.vector_store import VectorStore

store = VectorStore(384)


def ingest_folder(folder):
    print("\nINGESTING:", folder)
    for file in os.listdir(folder):
        print("Found:", file)

        if ".pdf" not in file.lower():
            continue

        path = os.path.join(folder, file)

        text = process_document(path)

        if not text or len(text.strip()) < 50:
            print(f"Skipping empty document: {file}")
            continue

        chunks = chunk_text(text)

        if not chunks:
            print(f"No chunks generated: {file}")
            continue

        embeddings = generate_embeddings(chunks)

        if len(embeddings) == 0:
            print(f"No embeddings generated: {file}")
            continue

        store.add(embeddings, chunks, source=folder)

        print(f"Processed {file} -> {len(chunks)} chunks")

if __name__ == "__main__":

    ingest_folder("data/raw/npci")

    ingest_folder("data/raw/rbi")

    store.save()