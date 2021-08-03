def solve(s):
    t = s[::-1]
    return sum(x != y for x, y in zip(s, t)) == 2 or (s != t and len(s) == 2) or (len(t) % 2 == 1 and t[:len(t) // 2] == s[:len(t) // 2])
