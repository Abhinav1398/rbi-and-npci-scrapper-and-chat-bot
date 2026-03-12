import faiss
import numpy as np
import pickle
import os

class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatIP(dim)
        self.docs = []

    def add(self, embeddings, docs, source):
        embeddings = np.array(embeddings).astype("float32")

        if embeddings.ndim == 1:
            embeddings = embeddings.reshape(1, -1)

        if embeddings.shape[0] == 0:
            return

        self.index.add(embeddings)

        for d in docs:
            self.docs.append({
                "text": d,
                "source": source
            })

    def save(self):
        os.makedirs("vector_store", exist_ok=True)
        faiss.write_index(self.index, "vector_store/faiss.index")

        with open("vector_store/docs.pkl", "wb") as f:
            pickle.dump(self.docs, f)