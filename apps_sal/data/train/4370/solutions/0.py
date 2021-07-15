def gen(n, d):
    if d == 0 or n == 1:
        yield [d]*n
    else:
        for x in range(d+1):
            for y in gen(n-1, d-x):
                yield [x] + y

def indices(n, d):
    return list(gen(n, d))
