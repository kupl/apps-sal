def cyclic_string(s):
    return next((i for (i, _) in enumerate(s[1:], 1) if s.startswith(s[i:])), len(s))
