def main():
    input()
    hh = list(map(int, input().split()))
    for f in (True, False):
        m = 1
        for (i, h) in enumerate(hh):
            if h > m:
                hh[i] = m
            else:
                m = h
            m += 1
        if f:
            hh.reverse()
    print(max(hh))


def __starting_point():
    main()


__starting_point()
