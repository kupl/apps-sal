def transform(c):
    d = chr(219 - ord(c.lower()))
    return d if c.islower() else d.upper()


def decode(s):
    return "Input is not a string" if not isinstance(s, str) else ''.join(transform(c) if c.isalpha() else c for c in s)
