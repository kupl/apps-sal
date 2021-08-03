def char_to_ascii(s): return None if len(s) == 0 else {c: ord(c) for c in s if c.isalpha()}
