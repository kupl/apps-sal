def even_chars(stg):
    return list(stg[1::2]) if 1 < len(stg) < 101 else 'invalid string'
