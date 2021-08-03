def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        return 'invalid string'
    else:
        return [st[i] for i in range(1, len(st), 2)]
