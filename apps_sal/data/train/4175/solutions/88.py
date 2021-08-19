def repeater(s, n):
    return s + repeater(s, n - 1) if n > 0 else ''
