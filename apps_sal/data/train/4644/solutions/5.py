def char_to_ascii(stg):
    return {c: ord(c) for c in set(stg) if c.isalpha()} if stg else None
