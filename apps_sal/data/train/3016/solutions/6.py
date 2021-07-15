def minor_or_major(s):
    p = ['C D EF G A B'.find(n[0]) + ('#' in n) - ('b' in n) for n in s.split()]
    return {(3,4): 'Minor', (4,3): 'Major'}.get(tuple((b - a + 12) % 12 for a,b in zip(p, p[1:])), 'Not a chord')
