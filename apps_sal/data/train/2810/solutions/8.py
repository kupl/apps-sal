def solve(words):
    return [sum(a == b for a, b in zip(w.lower(), 'abcdefghijklmnopqrstuvwxyz')) for w in words]
