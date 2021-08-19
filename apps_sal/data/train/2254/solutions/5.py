def main():
    (n, q) = list(map(int, input().split()))
    (vol, tot, l, res) = ([0] * (n + 1), [0] * (n + 1), [], [])
    z = m = 0
    for _ in range(q):
        (t, x) = list(map(int, input().split()))
        if t == 1:
            l.append(x)
            tot[x] += 1
            vol[x] += 1
            z += 1
        elif t == 2:
            z -= vol[x]
            vol[x] = 0
        elif m < x:
            (r, m) = (list(range(m, x)), x)
            for i in r:
                x = l[i]
                tot[x] -= 1
                if vol[x] > tot[x]:
                    vol[x] -= 1
                    z -= 1
        res.append(z)
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
