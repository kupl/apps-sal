def get_weight(name):
    return sum(ord(a) for a in name.swapcase() if a.isalpha())
