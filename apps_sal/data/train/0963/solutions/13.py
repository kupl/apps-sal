for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    def func(l):
        m = max(l)
        m = l.index(m)
        if m == len(l) - 1 or m == 0:
            return 1
        ll = l[:m]
        rl = l[m + 1:]
        return 1 + min(func(rl), func(ll))
    print(func(l))
