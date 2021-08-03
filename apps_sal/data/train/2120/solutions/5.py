def main():
    n, res, le, tot = int(input()), [], 1, 0
    l, base = [0] * (n + 2), [0] * (n + 2)
    for _ in range(n):
        s = input()
        c = s[0]
        if c == '1':
            a, x = list(map(int, s[2:].split()))
            base[a] += x
            tot += a * x
        elif c == '2':
            l[le] = x = int(s[2:])
            tot += x
            le += 1
        else:
            x = base[le]
            if x:
                base[le] = 0
                tot -= x
                le -= 1
                base[le] += x
            else:
                le -= 1
            tot -= l[le]

        res.append(tot / le)
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
