def solve(n):
    res = float('inf')
    for x in range(1, int(n**0.5)+1):
        y, r = divmod(n, x)
        if not (r or x == y) and y-x & 1 ^ 1:
            res = min(res, y-x >> 1)
    return -1 if res == float('inf') else res**2
