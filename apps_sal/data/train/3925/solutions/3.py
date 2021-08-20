def is_john_lying(a, b, s):
    ab = abs(a) + abs(b)
    return ab <= s and ab & 1 == s & 1
