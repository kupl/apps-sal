def is_john_lying(a, b, c):
    a, b = abs(a), abs(b)
    return c >= a + b and (c - a - b) % 2 ^ 1
