def similarity(a, b):
    (a, b) = (set(a), set(b))
    return len(a & b) / len(a | b)
