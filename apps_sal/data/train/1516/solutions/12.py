def main():
    Mod = 10 ** 9 + 7
    t = int(input())
    for i in range(t):
        (n, k) = list(map(int, input().split()))
        a = (k - 1) % (n - 1)
        d = n - 1
        num = (k - 1) // (n - 1) + 1
        res = num * (2 * a + (num - 1) * d) // 2
        print(res % Mod)


def __starting_point():
    main()


__starting_point()
