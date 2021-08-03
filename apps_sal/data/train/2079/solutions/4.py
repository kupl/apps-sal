def main():
    from collections import Counter
    d = Counter()
    for _ in range(int(input())):
        c, *l = input().split()
        if c == "1":
            v, u, w = list(map(int, l))
            while u != v:
                if u < v:
                    d[v] += w
                    v //= 2
                else:
                    d[u] += w
                    u //= 2
        else:
            w = 0
            v, u = list(map(int, l))
            while u != v:
                if u < v:
                    w += d[v]
                    v //= 2
                else:
                    w += d[u]
                    u //= 2
            print(w)


def __starting_point():
    main()


__starting_point()
