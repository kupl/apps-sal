def array_info(x):

    if not x:
        return 'Nothing in the array!'

    a, b, c, d, e = [len(x)],\
        [len([y for y in x if isinstance(y, int)])],\
        [len([y for y in x if isinstance(y, float)])],\
        [len([y for y in x if isinstance(y, str) and y != ' '])],\
        [len([y for y in x if y == ' '])]

    return [a if a[0] != 0 else [None],
            b if b[0] != 0 else [None],
            c if c[0] != 0 else [None],
            d if d[0] != 0 else [None],
            e if e[0] != 0 else [None]]
