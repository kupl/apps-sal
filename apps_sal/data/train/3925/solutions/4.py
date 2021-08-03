def is_john_lying(a, b, s):
    return abs(a) + abs(b) - s <= 0 and (abs(a) + abs(b) - s) % 2 == 0
