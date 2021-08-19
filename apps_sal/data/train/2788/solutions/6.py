def even_chars(st):
    return [x for (i, x) in enumerate(st) if i % 2 == 1] if 101 > len(st) > 1 else 'invalid string'
