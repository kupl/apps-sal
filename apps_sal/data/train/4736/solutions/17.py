def how_many_bees(h):
    return (lambda m, tm: sum((sum((q.count(a) for q in b)) for a in ['bee', 'eeb'] for b in [m, tm])))([''.join(x) for x in h] if h else [], [''.join([h[p][q] for p in range(len(h))]) for q in range(0 if len(h) == 0 else len(h[0]))] if h else [])
