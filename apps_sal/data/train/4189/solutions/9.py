def highest_value(a, b):
    return a if sum((ord(c) for c in a)) >= sum((ord(c) for c in b)) else b
