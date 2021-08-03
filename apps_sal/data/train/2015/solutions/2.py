def main():
    n, res, vv, dd, pp = int(input()), [], [], [], []
    for i in range(n):
        v, d, p = map(int, input().split())
        vv.append(v)
        dd.append(d)
        pp.append(p)
    for i, v, p in zip(range(1, n + 1), vv, pp):
        if p >= 0:
            res.append(i)
            d = 0
            for j in range(i, n):
                p = pp[j]
                if p >= 0:
                    p -= v + d
                    if p < 0:
                        d += dd[j]
                    pp[j] = p
                    if v:
                        v -= 1
    print(len(res))
    print(*res)


def __starting_point():
    main()


__starting_point()
