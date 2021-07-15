def solve(n, k):
    res = list(range(n))
    for i in range(n):
        res = res[:i] + res[i:][::-1]
    return res.index(k)
