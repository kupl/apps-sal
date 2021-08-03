def solve(arr):
    res = []
    [res.append(c) for c in arr[::-1] if c not in res]
    return res[::-1]
