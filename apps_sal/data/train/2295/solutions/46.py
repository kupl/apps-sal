def main():
    n = int(input())
    s = 0
    x = 10 ** 10
    for _ in range(n):
        (a, b) = map(int, input().split())
        if a > b:
            if x > b:
                x = b
        s += a
    if x == 10 ** 10:
        print(0)
    else:
        print(s - x)


def __starting_point():
    main()


__starting_point()
