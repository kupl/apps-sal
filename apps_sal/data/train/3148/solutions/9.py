D = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}

def simplify(s):
    q, c, w = set(), (0, 0), [(0, 0)]
    for i, k in enumerate(s):
        p = D[k]
        c = (c[0]+p[0], c[1]+p[1])
        if c in w:
            j = w.index(c)
            w[j:i+1] = [-1] * (i-j+1)
            q |= set(range(j, i+1))
        w.append(c)
    return ''.join(x for i, x in enumerate(s) if i not in q)
