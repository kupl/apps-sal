def main():
    n = int(input())
    (xs, ys, clones) = ({}, {}, {})
    res = 0
    clones_num = 0
    points = []
    for _ in range(n):
        (x, y) = list(map(int, input().split()))
        if x not in xs:
            xs[x] = 0
        if y not in ys:
            ys[y] = 0
        if (x, y) not in clones:
            clones[x, y] = 0
        xs[x] += 1
        ys[y] += 1
        clones[x, y] += 1
    for c in clones:
        n = clones[c]
        clones_num += n * (n - 1) // 2
    for x in xs:
        n = xs[x]
        res += n * (n - 1) // 2
    for y in ys:
        n = ys[y]
        res += n * (n - 1) // 2
    print(res - clones_num)


def __starting_point():
    main()


__starting_point()
