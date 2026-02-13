import faiss


def search_similar_names(
    query_vector,
    faiss_index,
    names: list[str],
    top_k: int = 5,
    min_score: float = 0.4
):
    query_vector = query_vector.toarray().astype("float32")

    # Normalize query for cosine similarity
    faiss.normalize_L2(query_vector)

    scores, indices = faiss_index.index.search(query_vector, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if score >= min_score:
            results.append({
                "name": names[idx],
                "score": round(float(score), 4)
            })

    return results
