def main():
    from math import factorial as f
    (n, res) = (0, 1)
    for _ in range(int(input())):
        m = int(input())
        res = res * f(n + m - 1) // f(n) // f(m - 1) % 1000000007
        n += m
    print(res)


def __starting_point():
    main()


__starting_point()
