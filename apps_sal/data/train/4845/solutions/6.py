def fl(l):
    for x in l:
        if isinstance(x, list):
            for j in fl(x):
                yield j
        else:
            yield x


def sort_nested_list(a):
    numbers = iter(sorted(fl(a)))

    def b(n, a):
        return [next(n)if isinstance(c, int)else b(n, c)for c in a]
    return b(numbers, a)
