find_missing = lambda *a, C=__import__("collections").Counter: C.__sub__(*map(C, a)).popitem()[0]
