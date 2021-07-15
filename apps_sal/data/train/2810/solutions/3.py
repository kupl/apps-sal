def solve(arr):
    return [sum(i == ord(c) - ord('A') for i, c in enumerate(s.upper())) for s in arr]
