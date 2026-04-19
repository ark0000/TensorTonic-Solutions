def bag_of_words(corpus):
    vals={val for li in corpus for val in li}
    vocab= sorted((vals))
    vocabs={token:i for i,token in enumerate(vocab)}
    vectors=[]
    v=len(vocabs)
    for docs in corpus:
        vec=[0]*v
        for val in docs:
          index_val=vocabs[val]
          vec[index_val]+=1
        vectors.append(vec)
    return {"vocab": vocabs, "vectors": vectors}
        
    """
    Returns: dict
    """
    pass