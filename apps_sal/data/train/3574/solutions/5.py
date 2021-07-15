def Dragon(n):
    if not isinstance(n, int) or n < 0:
        return ''
    s = 'Fa'
    for _ in range(n):
        s = ''.join({'a': 'aRbFR', 'b': 'LFaLb'}.get(c, c) for c in s)
    return s.replace('a', '').replace('b', '')
