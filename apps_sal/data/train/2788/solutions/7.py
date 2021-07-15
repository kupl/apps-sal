def even_chars(s):
    return list(s[1::2]) if 2 <= len(s) <= 100 else 'invalid string'
