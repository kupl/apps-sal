def main():
    (n, m) = list(map(int, input().split()))
    f = [1] * n
    lang = [set(map(int, input().split()[1:])) for _ in range(n)]
    for (i, langi) in enumerate(lang):
        for (j, langj) in enumerate(lang[:i]):
            if f[j] and langj.intersection(langi):
                f[j] = 0
                langi.update(langj)
    print(sum(f) - any(lang))


def __starting_point():
    main()


__starting_point()
