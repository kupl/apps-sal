def is_john_lying(a, b, s):
    delta = abs(a) + abs(b) - s
    return delta <= 0 and delta % 2 == 0
