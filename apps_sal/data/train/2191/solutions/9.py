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
        if a <= res:
            break
        res = max(res, maxa % a, *tuple(b % a for b in x[2 * a - 1::a]))
    print(res)


def __starting_point():
    main()


__starting_point()
