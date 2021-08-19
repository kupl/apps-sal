def st2(x, y):
    l = int((x * y * 4 - 1) ** 0.5)
    return l - 1 - int(x != y)


def st3(x, y):
    (p, q) = (1, (max(x, y) + 1) * 2)
    while q - p > 1:
        m = (p + q) // 2
        if m * m < x * y * 4:
            p = m
        else:
            q = m
    l = p
    return l - 1 - int(x != y)


def query(x, y):
    print(st3(x, y))


def main():
    n = int(input())
    for _ in range(n):
        (x, y) = map(int, input().split())
        query(x, y)


def __starting_point():
    main()


__starting_point()
