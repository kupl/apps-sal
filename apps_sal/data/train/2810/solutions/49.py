def solve(arr):
    return [sum((ord(c) - 97 == i) for i, c in enumerate(s.lower())) for s in arr]
