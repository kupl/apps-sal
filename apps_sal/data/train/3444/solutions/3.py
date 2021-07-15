def cyclic_string(s):
    length = len(s)
    for i in range(1, length + 1):
        if s in s[:i] * length:
            return i
