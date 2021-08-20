def even_chars(st):
    return list(st[1::2]) if 2 <= len(st) <= 100 else 'invalid string'
