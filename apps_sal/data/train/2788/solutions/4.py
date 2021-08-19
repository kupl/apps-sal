def even_chars(st):
    return list(st[1::2]) if len(st) > 1 and len(st) < 100 else 'invalid string'
