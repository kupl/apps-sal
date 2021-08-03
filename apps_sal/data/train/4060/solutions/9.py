def ant_bridge(a, t):
    t = t.replace('-.', '..').replace('.-', '..').strip('-')
    A, B = list(a), []
    while t:
        t = t.lstrip('-')[1:]
        B += [A.pop()if A else B.pop(0)]
    return ''.join(B[::-1] + A)
