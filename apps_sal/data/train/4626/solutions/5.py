decode = lambda s: "Input is not a string" if not isinstance(s, str) else "".join(chr(155 + 64*(96<ord(c)<123) - ord(c)) if c.isalpha() else c for c in s)
