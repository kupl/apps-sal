def is_triangle(a, b, c):
    s = sorted([a, b, c])
    return False if s[0] < 1 or sum(s[:-1]) <= s[2] else True
