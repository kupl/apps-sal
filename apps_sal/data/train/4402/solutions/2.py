def solve(s):
    return len(s) == len(set(s)) == ord(max(s)) - ord(min(s)) + 1
