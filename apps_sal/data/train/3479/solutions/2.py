def get_addends(num, x=1):
    yield (num,)
    for i in range(x, num // 2 + 1):
        for p in get_addends(num - i, i):
            yield ((i,) + p)


def part_const(n, k, num):
    return len([el for el in get_addends(n) if len(el) == k and num not in el])
