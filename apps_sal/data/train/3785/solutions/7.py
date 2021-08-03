def generate_diagonal(n, l):
    if n == 0:
        c = []
        while l > 0:
            c += [1]
            l -= 1
        return c
    if l == 0 and n == 0:
        return '[]'
    else:
        i = n + l
        q = []
        o = []

        def triangles():
            p = [1]
            while True:
                yield p
                p = [1] + [p[x] + p[x + 1] for x in range(len(p) - 1)] + [1]
        for t in triangles():
            if i > 0:
                i -= 1
                q.append(t)
            else:
                break
        for t in range(l):
            r = q[n][t]
            n += 1
            o.append(r)
        return o
