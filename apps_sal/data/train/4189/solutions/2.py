def highest_value(a, b):
    return b if sum(ord(x) for x in b) > sum(ord(x) for x in a) else a
