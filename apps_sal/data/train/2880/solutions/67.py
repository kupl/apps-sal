def func(m, step):
    if len(str(m)) <= 2:
        return (m, step)
    else:
        a = int(str(m)[:-1])
        b = int(str(m)[-1])
        return func(a - 2 * b, step + 1)


def seven(m):
    return func(m, 0)
