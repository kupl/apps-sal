def Dragon(n):
    if not isinstance(n, int) or n < 0:
        return ''
    s = 'Fa'
    for i in range(n):
        s = 'aRbFR'.join(t.replace('b', 'LFaLb') for t in s.split('a'))
    return s.replace('a', '').replace('b', '')

