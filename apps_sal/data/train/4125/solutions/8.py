def get_weight(name):
    return sum((ord(x) for x in filter(str.isalpha, name.swapcase())))
