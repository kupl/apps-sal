def solve():
    c = list(map(int, input().strip().split()))
    n = len(c)
    if n <= 2:
        print(1)
        return
    k = (n + 1) // 2
    r = [[], []]
    for i in range(n):
        if i % 2 == 0:
            r[0].append(c[i])
        else:
            r[1].append(c[i])
    if len(r[1]) < k:
        r[1].append(0)
    r[0].append(0)
    r[1].append(0)
    while k > 0:
        p = []
        for i in range(1, k + 1):
            p.append(r[-1][0] * r[-2][i] - r[-1][i] * r[-2][0])
        r.append(p + [0])
        k -= 1
    r = [x[0] for x in r]
    (atleastz, allz) = (0, 1)
    for x in r:
        if x == 0:
            atleastz = 1
        else:
            allz = 0
    if atleastz:
        if allz:
            print(1)
        else:
            print(0)
        return
    for i in range(1, len(r)):
        if r[i] * r[i - 1] < 0:
            print(0)
            return
    print(1)


def main():
    t = int(input().strip())
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
