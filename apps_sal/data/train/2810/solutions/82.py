def solve(arr):
    return [sum(ord(c) - ord('a') == i for i, c in enumerate(s.lower())) for s in arr]
