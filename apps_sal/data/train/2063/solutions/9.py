def main():
    def root(a):
        b = f[a]
        while b != a:
            a, b = b, f[b]
        return a

    n, m = list(map(int, input().split()))
    f = list(range(n))
    lang = []
    for _ in range(n):
        ll = [False] * m
        for i in map(int, input().split()[1:]):
            ll[i - 1] = True
        lang.append(ll)
    for i, langi in enumerate(lang):
        for j in range(i):
            if j == root(j) and any(a and b for a, b in zip(lang[i], lang[j])):
                f[j] = i
                for _, flag in enumerate(lang[j]):
                    langi[_] |= flag
    print(sum(i == root(i) for i in range(n)) - any(map(any, lang)))


def __starting_point():
    main()


__starting_point()
