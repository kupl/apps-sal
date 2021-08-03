def main():
    n, l = int(input()), list(map(int, input().split()))
    if not (n & 1):
        l.append(0)
    l.append(150001)
    i, b, c, fails0, fails1 = 0, 0, 150001, [], []
    try:
        while True:
            a, b, c = b, c, l[i]
            if a >= b or b <= c:
                if len(fails0) + len(fails1) > 5:
                    print(0)
                    return
                fails1.append(i - 1)
            i += 1
            a, b, c = b, c, l[i]
            if a <= b or b >= c:
                if len(fails0) + len(fails1) > 5:
                    print(0)
                    return
                fails0.append(i - 1)
            i += 1
    except IndexError:
        fails, res = fails0 + fails1, 0
    for i in fails:
        a = l[i]
        for j in range(n):
            f = fails1 if j & 1 else fails0
            f.append(j)
            l[i], l[j] = l[j], a
            if (all(l[b - 1] > l[b] < l[b + 1] for b in fails0)
                    and all(l[b - 1] < l[b] > l[b + 1] for b in fails1)):
                res += 1 if j in fails else 2
            l[j] = l[i]
            del f[-1]
        l[i] = a
    print(res // 2)


def __starting_point():
    main()


__starting_point()
