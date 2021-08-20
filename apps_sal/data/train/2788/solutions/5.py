def even_chars(st):
    return list(st[1::2]) if 1 < len(st) < 101 else 'invalid string'
