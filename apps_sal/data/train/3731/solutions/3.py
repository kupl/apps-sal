def square_sums_row(n):

    def dfs():
        if not n:
            yield r
        for p in tuple(n):
            if not r or not (r[-1] + p) ** 0.5 % 1:
                r.append(p)
                n.discard(p)
                yield from dfs()
                n.add(r.pop())
    (n, r) = (set(range(1, n + 1)), [])
    return next(dfs(), False)
