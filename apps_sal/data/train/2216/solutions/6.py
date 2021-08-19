def main():
    (l, xyz, res) = ([(0, 0, 0)], [0, 0, 0], [])
    for c in input():
        xyz[ord(c) - 120] += 1
        l.append(tuple(xyz))
    for _ in range(int(input())):
        (a, b) = list(map(int, input().split()))
        if b - a > 1:
            xyz = [i - j for (i, j) in zip(l[b], l[a - 1])]
            res.append(('NO', 'YES')[max(xyz) - min(xyz) < 2])
        else:
            res.append('YES')
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
