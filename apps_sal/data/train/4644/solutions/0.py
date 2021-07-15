def char_to_ascii(string):
    return {c: ord(c) for c in set(string) if c.isalpha()} if len(string) else None
