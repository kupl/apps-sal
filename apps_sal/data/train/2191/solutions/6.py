def main():
    input()
    aa = sorted(set(map(int, input().split())))
    x = []
    b = res = 0
    for a in aa:
        x += [b] * (a - b)
        b = a
    x.append(b)
    maxa = aa.pop()
    for a in reversed(aa):
        if a < res:
            break
        for b in range(2 * a - 1, maxa, a):
            res = max(res, x[b] % a)
        res = max(res, maxa % a)
    print(res)


def __starting_point():
    main()


__starting_point()
