def get_weight(name):
    return sum((ord(c.swapcase()) for c in name if c.isalpha()))
