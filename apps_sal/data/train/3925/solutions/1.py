def is_john_lying(a, b, s):
    (a, b) = (abs(a), abs(b))
    return s - a - b >= 0 and (s - a - b) % 2 == 0
