from sklearn.feature_extraction.text import TfidfVectorizer


class CharacterEmbedder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            analyzer="char",
            ngram_range=(2, 4)
        )
        self.is_fitted = False

    def fit(self, texts: list[str]):
        self.vectorizer.fit(texts)
        self.is_fitted = True

    def transform(self, texts: list[str]):
        if not self.is_fitted:
            raise RuntimeError("Embedder must be fitted before calling transform")

        return self.vectorizer.transform(texts)
