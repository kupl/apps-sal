def inverse_slice(items, a, b):
    splice1 = items[:a]
    splice2 = items[b:]
    return splice1 + splice2
