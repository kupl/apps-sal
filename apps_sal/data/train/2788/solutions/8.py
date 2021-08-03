def even_chars(st):
    return len(st) < 101 and list(st[1::2]) or 'invalid string'
