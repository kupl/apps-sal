def similarity(a, b):
    # coding and coding..
    return float(len(set(a) & set(b))) / len(set(a) | set(b))
