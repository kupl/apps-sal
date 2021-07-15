def char_to_ascii(s):
    if s: return {c: ord(c) for c in set(s) if c.isalpha()}

