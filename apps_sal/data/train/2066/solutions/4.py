def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    print(min((b - a for (a, b) in zip(l, l[n // 2:]))))


def __starting_point():
    main()


__starting_point()
