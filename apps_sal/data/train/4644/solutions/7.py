char_to_ascii = lambda s: None if len(s) == 0 else {c: ord(c) for c in s if c.isalpha()}
