def main():
    n, l, r, Ql, Qr = list(map(int, input().split()))
    ww = list(map(int, input().split()))
    work = sum(ww) * r + (n - 1) * Qr
    res, penalty = [work], Qr * 2
    l -= r
    for w in ww[:(n - 1) // 2]:
        work += l * w - penalty
        res.append(work)
    penalty = Ql * 2
    work += l * ww[(n - 1) // 2]
    if n & 1:
        res.append(work)
    else:
        work -= Qr
        res.append(work)
        work -= Ql
    for w in ww[(n + 1) // 2:]:
        work += l * w + penalty
        res.append(work)
    print(min(res))


def __starting_point():
    main()


__starting_point()
