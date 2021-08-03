def alphabetic(s):
    return all(ord(a) <= ord(b) for a, b in zip(s, s[1:]))
