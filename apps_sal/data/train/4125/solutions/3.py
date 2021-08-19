def get_weight(name):
    return sum((ord(x) for x in name.swapcase() if x.isalpha()))
