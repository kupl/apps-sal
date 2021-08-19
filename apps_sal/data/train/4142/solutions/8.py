def solve(arr):
    arr = [''.join(sorted(list(set(x)))) for x in arr]
    return sorted((sum((i for (i, y) in enumerate(arr) if x == y)) for x in set(arr) if arr.count(x) >= 2))
