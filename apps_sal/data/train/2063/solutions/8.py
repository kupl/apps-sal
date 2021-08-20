def main():

    def root(a):
        b = f[a]
        while b != a:
            (a, b) = (b, f[b])
        return a
    (n, m) = list(map(int, input().split()))
    f = list(range(n))
    lang = []
    for _ in range(n):
        lang.append(set(map(int, input().split()[1:])))
    for i in range(n):
        for j in range(i):
            if j == root(j) and lang[j].intersection(lang[i]):
                f[j] = i
                lang[i].update(lang[j])
    print(sum((i == root(i) for i in range(n))) - any(lang))


def __starting_point():
    main()


__starting_point()
