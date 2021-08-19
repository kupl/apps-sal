def solve(st, k):
    n = len(st) - k
    return max((int(st[i:i + n]) for i in range(len(st))))
