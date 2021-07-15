def main():
    def root(x):
        a, b = x, f[x]
        while b != a:
            a, b = b, f[b]
        return a == x

    n, m = list(map(int, input().split()))
    f = list(range(n))
    lang = []
    for _ in range(n):
        lang.append(set(map(int, input().split()[1:])))
    for i, langi in enumerate(lang):
        for j in range(i):
            if root(j) and lang[j].intersection(langi):
                f[j] = i
                langi.update(lang[j])
    print(sum(root(i) for i in range(n)) - any(lang))


def __starting_point():
    main()

__starting_point()
