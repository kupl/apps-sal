def main():
    input()
    aa = sorted(set(map(int, input().split())))
    x = []
    b = res = 0
    for a in aa:
        if b != a:
            for _ in range(b, a):
                x.append(b)
            b = a
    x.append(b)
    maxa = aa.pop()
    for a in reversed(aa):
        if a < res:
            break
        for b in range(2 * a - 1, maxa + 2 * a, a):
            res = max(res, x[min(b, maxa)] % a)
    print(res)


def __starting_point():
    main()


__starting_point()
