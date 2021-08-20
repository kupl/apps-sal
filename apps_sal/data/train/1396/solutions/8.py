def main():
    t = int(input())
    for __ in range(t):
        (n, m, x, y) = list(map(int, input().split()))
        if n == m and m <= 1:
            print('Chefirnemo')
        elif (n - 1) % x == 0 and (m - 1) % y == 0:
            print('Chefirnemo')
        elif (n - 2) % x == 0 and (m - 2) % y == 0 and (min(n, m) > 1):
            print('Chefirnemo')
        else:
            print('Pofik')


def __starting_point():
    main()


__starting_point()
