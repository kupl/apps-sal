def main():
    s, w = ['', *input()], input()
    l = list(map(int, input().split()))
    lo, hi = 0, len(s) - len(w)
    while lo < hi:
        mid, t = (lo + hi) // 2, s[:]
        for i in l[:mid]:
            t[i] = ''
        try:
            i = 1
            for c in w:
                while c != t[i]:
                    i += 1
                i += 1
        except IndexError:
            hi = mid
        else:
            lo = mid + 1
    print(lo - 1)


def __starting_point():
    main()


__starting_point()
