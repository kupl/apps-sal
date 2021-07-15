def solve(s):
    return len(s) == ord(max(s)) - ord(min(s)) + 1
