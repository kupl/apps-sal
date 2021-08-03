def sum_pow_dig_seq(n, e, k):
    path = [n]
    while True:
        n = sum(int(d)**e for d in str(n))
        if n in path:
            break
        path.append(n)
    h = path.index(n)
    loop = path[h:]
    return [h, loop, len(loop), loop[(k - h) % len(loop)]]
