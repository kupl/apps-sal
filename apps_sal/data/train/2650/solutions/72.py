def main():
    (n, l) = list(map(int, input().split()))
    s = sorted([input() for i in range(n)])
    print(''.join(s))


def __starting_point():
    main()


__starting_point()
