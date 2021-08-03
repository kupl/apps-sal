def f(xs, i, changed):
    if i and int(''.join(map(str, xs[:i]))) % i:
        return
    if i == len(xs):
        return int(''.join(map(str, xs)))

    prev = xs[i]
    for x in range(0 if changed else prev, 10):
        xs[i] = x
        res = f(xs, i + 1, changed or x != prev)
        if res:
            return res
    xs[i] = prev


def next_num(n):
    res = f(list(map(int, str(n + 1))), 0, False)
    if res:
        return res
    s = '1' + '0' * len(str(n))
    return f(list(map(int, s)), 0, False)
