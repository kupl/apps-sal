def solve(arr):
    d = {}
    for i, e in enumerate(arr):
        d[e] = i
    return sorted(set(arr), key=d.get)
