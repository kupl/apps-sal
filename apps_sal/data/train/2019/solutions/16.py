def main():
    n = int(input())
    aa = list(map(int, input().split()))
    m = max(aa)
    d = m * n - sum(aa)
    if m > d:
        m += (m - d + n - 2) // (n - 1)
    print(m)


def __starting_point():
    main()


__starting_point()
