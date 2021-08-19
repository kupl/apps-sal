def main():
    (l, base, res, le, tot) = ([0] * 200001, [0] * 200001, [], 1, 0)
    for _ in range(int(input())):
        s = input()
        c = s[0]
        if c == '1':
            (a, x) = list(map(int, s[2:].split()))
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
