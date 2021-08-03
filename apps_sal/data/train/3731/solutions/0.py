def square_sums_row(n):

    def dfs():
        if not inp:
            yield res
        for v in tuple(inp):
            if not res or not ((res[-1] + v)**.5 % 1):
                res.append(v)
                inp.discard(v)
                yield from dfs()
                inp.add(res.pop())

    inp, res = set(range(1, n + 1)), []
    return next(dfs(), False)
