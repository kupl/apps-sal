def has_unique_chars(s):
    return len(s) <= 128 and len(s) == len(set(s))
