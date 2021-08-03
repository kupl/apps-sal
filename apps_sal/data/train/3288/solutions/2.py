def solve(st, k):
    return max([int(st[i:i + len(st) - k]) for i in range(len(st))])
