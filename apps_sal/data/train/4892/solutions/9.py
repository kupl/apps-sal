def find_biggTriang(P, m=0, c=0):
    (Z, V, l) = ([], set(), len(P))
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                ((x, y), (u, v), (p, q)) = (P[i], P[j], P[k])
                s = abs((u - x) * (q - y) - (v - y) * (p - x)) / 2
                if s:
                    V.add((i, j, k))
                T = [[x, y], [u, v], [p, q]]
                if m < s:
                    (Z, m) = ([T], s)
                elif m == s:
                    Z += [T]
                c += 1
    return [l, c, len(V), 1 < len(Z) and Z or Z[0], m]
