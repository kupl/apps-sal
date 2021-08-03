def mutations(a, b, w, f):
    z, t, i, P, U = -1, -1, f ^ 1, [a, b], {w}
    while 1:
        i ^= 1
        u = next((x for x in P[i]if x not in U and sum(p == q for p, q in zip(x, w)) == 3 and len(set(x)) == 4), '')
        if u:
            w, z, U = u, i, U | {u}
            if t != -1:
                return z
        else:
            if t == i ^ 1:
                return z
            t = i
