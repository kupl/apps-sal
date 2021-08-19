def is_keith_number(n):

    def rec(ds, i):
        d = sum(ds)
        ds = ds[1:]
        ds.append(d)
        return i if d == n else False if d > n else rec(ds, i + 1)
    return False if n < 10 else rec([int(x) for x in list(str(n))], 1)
