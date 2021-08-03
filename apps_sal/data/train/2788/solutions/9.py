def even_chars(st):
    # your code here
    return [st[i] for i in range(1, len(st), 2)] if 1 < len(st) < 100 else "invalid string"
