from collections import Counter

def solve(s):
    return any(len(set(Counter(s[:i] + s[i+1:]).values())) == 1 for i in range(len(s)))
