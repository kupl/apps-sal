def check(n, m, s, v):
    mi = 0
    for i in range(n):
        if v[i] + s < mi:
            return False
        if v[i] > mi:
            if (v[i] + s) % m >= mi:
                if v[i] <= (v[i] + s) % m:
                    mi = v[i]
            else:
                mi = v[i]

    return True


def __starting_point():
    n, m = list(map(int, input().split()))
    v = list(map(int, input().split()))

    l = 0
    r = m
    while l < r:
        s = (l + r) // 2
        if check(n, m, s, v):
            r = s
        else:
            l = s + 1

    print(l)


__starting_point()
