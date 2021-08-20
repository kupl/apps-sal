def rs():
    return input().strip()


def ri():
    return int(input())


def ria():
    return list(map(int, input().split()))


def ia_to_s(a):
    return ' '.join([str(s) for s in a])


def solve(a, b):
    mi = min(a, b)
    ma = max(a, b)
    s = max(2 * mi, ma)
    return s * s


def main():
    for _ in range(ri()):
        (a, b) = ria()
        print(solve(a, b))


def __starting_point():
    main()


__starting_point()
