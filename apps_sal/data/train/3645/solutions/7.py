def diff(a, b):
    (a, b) = (set(a), set(b))
    return sorted((a - b).union(b - a))
