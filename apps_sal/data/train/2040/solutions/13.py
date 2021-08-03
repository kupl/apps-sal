from fractions import Fraction


def main():
    n, H = map(int, input().split())

    s = Fraction(H, 2 * n)

    h2 = []
    for m in range(1, n):
        S = s * m
        h2.append(S * 2 * H)

    for x in h2:
        print("{:.12f}".format(x ** 0.5), end=' ')


def __starting_point():
    main()


__starting_point()
