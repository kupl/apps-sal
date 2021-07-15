def solve(s, k):
    n = len(s) - k
    return max(int(s[i:i+n]) for i in range(0, k + 1))
