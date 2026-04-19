import numpy as np

def embedding_similarity(query, candidates, metric="cosine", k=1):
    q = np.array(query)
    C = np.array(candidates)

    scores = []
    for idx, c in enumerate(C):
        if metric == "cosine":
            s = np.dot(q, c) / (np.linalg.norm(q) * np.linalg.norm(c))
        elif metric == "dot":
            s = np.dot(q, c)
        elif metric == "euclidean":
            s = -np.linalg.norm(q - c)
        else:
            raise ValueError("Unknown metric")
        scores.append((idx, s))

    scores.sort(key=lambda x: (-x[1], x[0]))

    return [idx for idx, _ in scores[:k]]