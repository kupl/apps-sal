import sys


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n = int(input())

    if n <= 2:
        k = 1
        ans = [1] * n
        print(k)
        print(*ans)
    else:
        k = 2
        ans = color(n)
        print(k)
        print(*ans)


def color(n):
    res = [1] * (n + 2)  # 0, 1, 2, 3, ..., n + 1
    for p in range(2, n + 2):
        if res[p] != 1:
            continue
        for q in range(p * p, n + 2, p):
            res[q] = 2

    # debug(res, locals())

    return res[2:]


def __starting_point():
    solve()


__starting_point()
