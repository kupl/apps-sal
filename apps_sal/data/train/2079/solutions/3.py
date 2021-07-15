def main():
    d = {}
    for _ in range(int(input())):
        c, *l = input().split()
        if c == "1":
            v, u, w = list(map(int, l))
            while u != v:
                if u < v:
                    d[v] = d.get(v, 0) + w
                    u, v = v // 2, u
                else:
                    d[u] = d.get(u, 0) + w
                    u //= 2
        else:
            res = 0
            v, u = list(map(int, l))
            while u != v:
                if u < v:
                    res += d.get(v, 0)
                    u, v = v // 2, u
                else:
                    res += d.get(u, 0)
                    u //= 2
            print(res)


def __starting_point():
    main()

__starting_point()
