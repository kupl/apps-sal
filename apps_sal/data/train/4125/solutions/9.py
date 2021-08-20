def get_weight(name):
    return sum((ord(n.swapcase()) for n in name if n.isalpha()))
