def encode(s):
    return "".join(['1', '0'][ord(x) % 2] if x.isalpha() else x for x in s.lower())
