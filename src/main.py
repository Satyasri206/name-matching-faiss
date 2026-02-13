from src.data_loader import load_names
from src.embedder import CharacterEmbedder
from src.vector_index import FaissIndex
from src.similarity_search import search_similar_names


DATASET_PATH = "data/names_dataset.json"
INDEX_PATH = "embeddings/names.index"


def main():
    print("Loading names dataset...")
    names = load_names(DATASET_PATH)

    print("Creating character-level embeddings...")
    embedder = CharacterEmbedder()
    embedder.fit(names)
    name_vectors = embedder.transform(names)

    print("Building FAISS index...")
    faiss_index = FaissIndex(dimension=name_vectors.shape[1])
    faiss_index.add_vectors(name_vectors)
    faiss_index.save(INDEX_PATH)

    while True:
        user_input = input("\nEnter a name (or type 'exit'): ").strip()
        if user_input.lower() == "exit":
            break

        query_vector = embedder.transform([user_input])
        results = search_similar_names(query_vector, faiss_index, names)

        print("\nBest Match:")
        print(f"{results[0]['name']} (score: {results[0]['score']})")

        print("\nTop Matches:")
        for i, res in enumerate(results, start=1):
            print(f"{i}. {res['name']} - {res['score']}")


if __name__ == "__main__":
    main()
