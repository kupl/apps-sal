q = int(input())
for _ in range(q):
    n = int(input())
    t = list(map(int, input().split()))
    t_set = set(t)
    if len(t_set) == 1:
        print(1)
        print(*[1] * n)
        continue
    if n % 2 == 0:
        print(2)
        print(*[1, 2] * (n // 2))
        continue
    found = -1
    for (i, (t1, t2)) in enumerate(zip(t, t[1:] + [t[0]])):
        if t1 == t2:
            found = (i + 1) % n
    if found >= 0:
        print(2)
        r = []
        one = True
        for i in range(n):
            if i == found:
                one = not one
            if one:
                r += [1]
            else:
                r += [2]
            one = not one
        print(*r)
        continue
    print(3)
    r = [1, 2] * (n // 2) + [3]
    print(*r)
