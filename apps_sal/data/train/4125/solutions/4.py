def get_weight(s):
    return sum((ord(c) for c in s.swapcase() if c.isalpha()))
