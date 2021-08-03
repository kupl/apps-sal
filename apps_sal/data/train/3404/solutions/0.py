def solve(s, a, b):
    return s[:a] + s[a:b + 1][::-1] + s[b + 1:]
