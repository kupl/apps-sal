has_unique_chars = lambda s: not s[128:] and not s[len(set(s)):]

