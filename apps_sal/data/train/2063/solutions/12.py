def main():

    def root(x):
        (a, b) = (x, f[x])
        while b != a:
            (a, b) = (b, f[b])
        return a == x
    (n, m) = list(map(int, input().split()))
    f = list(range(n))
    lang = [set(map(int, input().split()[1:])) for _ in range(n)]
    for (i, langi) in enumerate(lang):
        for (j, langj) in enumerate(lang[:i]):
            if root(j) and langj.intersection(langi):
                f[j] = i
                langi.update(langj)
    print(sum((root(i) for i in range(n))) - any(lang))


def __starting_point():
    main()


__starting_point()
