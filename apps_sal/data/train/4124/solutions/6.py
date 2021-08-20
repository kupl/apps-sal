def has_unique_chars(s):
    return not s[len(set(s)):]
