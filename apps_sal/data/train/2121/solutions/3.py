def main():
    from sys import stdin
    n = int(input())
    l = sorted((list(map(int, stdin.read().splitlines()))), reverse=True)
    ita = iter(enumerate(l))
    i, a = next(ita)
    for b in l[(n + 1) // 2:]:
        if a >= b * 2:
            i, a = next(ita)
    print(n - i)


def __starting_point():
    main()

__starting_point()
