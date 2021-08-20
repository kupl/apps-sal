def solve2(p):
    P = (sum(p[0::2]), sum(p[1::2]))
    x = P[0] // 3 * 2 + (P[0] - 1) % 3
    y = P[1] // 3 * 2 + (P[1] - 1) % 3
    if x == y:
        if x == 0:
            print(0)
            return '0'
        elif x == 1:
            print(1)
            return '1'
        elif x > 0:
            print(x + 1)
            return str(x + 1)
        else:
            print(-x + 1)
            return str(1 - x)
    else:
        print(max(abs(x), abs(y)))
        return str(max(abs(x), abs(y)))


def main():
    N = int(input())
    Ps = [list(map(int, input().split())) for _ in range(N)]
    for P in Ps:
        solve2(P)


def __starting_point():
    main()


__starting_point()
