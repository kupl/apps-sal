def solve(s):
    all = sum(1 for i in range(len(s) // 2) if s[i] != s[-i-1])
    return all == 1 or all == 0 and len(s)%2 == 1
