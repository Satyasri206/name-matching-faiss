import faiss
import numpy as np
from pathlib import Path


class FaissIndex:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)

    def add_vectors(self, vectors):
        vectors = vectors.toarray().astype("float32")
        faiss.normalize_L2(vectors)
        self.index.add(vectors)

    def save(self, path: str):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(path))

    def load(self, path: str):
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"FAISS index not found at {path}")
        self.index = faiss.read_index(str(path))
