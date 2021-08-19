def hex_to_dec(s):
    return sum(((ord(x) - 87 if x.isalpha() else int(x)) * 16 ** i for (i, x) in enumerate(s[::-1])))
