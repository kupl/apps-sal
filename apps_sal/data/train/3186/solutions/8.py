def similarity(a, b):
    return float(len(set(a) & set(b))) / len(set(a) | set(b))
