def main():
    for _ in range(int(input())):
        (m, n) = map(int, input().split())
        if m == 1:
            print(0)
            continue
        if m == 2:
            print(n)
            continue
        a = (m - 1) + 2 * (n - 1)
        print(a)


def __starting_point():
    main()


__starting_point()
