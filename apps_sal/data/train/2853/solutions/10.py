def solve(arr):
    d = {x: i for (i, x) in enumerate(arr)}
    return sorted(d, key=d.get)
