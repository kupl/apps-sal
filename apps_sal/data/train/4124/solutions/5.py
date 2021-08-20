def has_unique_chars(s):
    return not s[128:] and (not s[len(set(s)):])
