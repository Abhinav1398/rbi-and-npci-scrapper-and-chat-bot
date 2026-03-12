import faiss
import pickle
import numpy as np
from src.ingestion.embedder import generate_embeddings


class QueryEngine:

    def __init__(self):

        self.index = faiss.read_index("vector_store/faiss.index")

        with open("vector_store/docs.pkl", "rb") as f:
            self.docs = pickle.load(f)

    def search(self, query, k=5):
        emb = generate_embeddings([query])
        emb = np.array(emb).astype("float32")

        scores, indices = self.index.search(emb, k)

        results = []
        for i in indices[0]:
            doc = self.docs[i]
            results.append(f"[SOURCE: {doc['source']}]\n{doc['text']}")
        return results