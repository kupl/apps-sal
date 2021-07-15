def is_john_lying(a, b, s):
    return s >= abs(a) + abs(b) and s % 2 == (a + b) % 2
