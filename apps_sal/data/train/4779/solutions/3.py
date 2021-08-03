def how_to_find_them(t):
    a = t.get('a', 0)
    b = t.get('b', 0)
    c = t.get('c', 0)
    if not c:
        t['c'] = (a**2 + b**2)**.5
    if not b:
        t['b'] = (c**2 - a**2)**.5
    if not a:
        t['a'] = (c**2 - b**2)**.5
    return t
