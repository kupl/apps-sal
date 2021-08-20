def tail_swap(ss):
    a = [s.split(':') for s in ss]
    (a[0][1], a[1][1]) = (a[1][1], a[0][1])
    return [':'.join(p) for p in a]
