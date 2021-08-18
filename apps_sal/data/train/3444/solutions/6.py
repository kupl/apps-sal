def cyclic_string(s):
    for i in range(1, len(s)):
        if s in s[:i] * (len(s) // i) * 2:
            return i
    return len(s)
