def cyclic_string(s):
    l = len(s)
    for i in range(1, l + 1):
        if s in s[:i] * l:
            return i
