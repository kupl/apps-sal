def solve(st, k):
    a = len(st) - k
    q = [st[i:i + a] for i in range(0, len(st))]
    r = [int(item) for item in q]
    return max(r)
