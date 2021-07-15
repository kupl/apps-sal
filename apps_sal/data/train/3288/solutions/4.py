def solve(st, k):
    window = len(st) - k
    return max(int(st[i:i+window]) for i in range(len(st)))
