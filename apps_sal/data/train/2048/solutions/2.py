def main():
    (n, k) = list(map(int, input().split()))
    l = sorted(map(int, input().split()))
    (lo, hi) = (l[0], l[-1])
    while lo < hi - 1:
        mid = (lo + hi) // 2
        t = k
        for x in l:
            if x > mid:
                lo = mid
                break
            t -= mid - x
            if t < 0:
                hi = mid
                break
        else:
            lo = mid
    m1 = lo
    (lo, hi) = (l[0], l[-1])
    l.reverse()
    while lo < hi - 1:
        mid = (lo + hi) // 2
        t = k
        for x in l:
            if x < mid:
                hi = mid
                break
            t -= x - mid
            if t < 0:
                lo = mid
                break
        else:
            hi = mid
    print(hi - m1 if hi > m1 else 1 if sum(l) % n else 0)


def __starting_point():
    main()


__starting_point()
