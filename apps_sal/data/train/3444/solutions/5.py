def cyclic_string(s):
    i = 1
    while not s.startswith(s[i:]):
        i += 1
    return i
