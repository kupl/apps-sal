def swap(st):
    return ''.join((c.upper() if c in 'aeiou' else c for c in st))
