def solve(st, k):
    length = len(st) - k
    return max(int(st[i:i + length]) for i in range(k + 1))
