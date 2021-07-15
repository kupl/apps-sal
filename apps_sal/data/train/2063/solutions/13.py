def main():
    n, m = list(map(int, input().split()))
    f = list(range(n))
    lang = [set(map(int, input().split()[1:])) for _ in range(n)]
    for i, langi in enumerate(lang):
        for j, langj in enumerate(lang[:i]):
            if f[j] == j and langj.intersection(langi):
                f[j] = i
                langi.update(langj)
    print(sum(i == x for i, x in enumerate(f)) - any(lang))


def __starting_point():
    main()

__starting_point()
