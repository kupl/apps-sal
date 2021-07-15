def main():
    n, k = map(int, input().split())
    a, b, c, d = (list(map(int, input().split())) for _ in 'abcd')
    ss, tt, n2, res = [*b, *c[::-1]], [*a, *d[::-1]], n * 2, []
    yx = [*[(2, i + 1) for i in range(n)], *[(3, i) for i in range(n, 0, -1)]]

    def park():
        for i, s, t, (y, x) in zip(range(n2), ss, tt, yx):
            if s == t != 0:
                ss[i] = 0
                res.append(f'{s} {(1, 4)[y == 3]} {x}')

    def rotate():
        start = ss.index(0)
        for i in range(start - n2, start - 1):
            s = ss[i] = ss[i + 1]
            if s:
                y, x = yx[i]
                res.append(f'{s} {y} {x}')
        ss[start - 1] = 0

    park()
    if all(ss):
        print(-1)
        return
    while any(ss):
        rotate()
        park()
    print(len(res), '\n'.join(res), sep='\n')


def __starting_point():
    main()

__starting_point()
