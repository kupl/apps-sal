def hot_singles(a, b):
    return sorted(set(a) ^ set(b), key=(a + b).index)
