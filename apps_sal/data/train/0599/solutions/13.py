for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    u = []
    k = 0
    t = max(l)
    for i in range(n):
        if l[i] == t:
            break
    y = i + 1
    while y != i:
        if l[y] != t:
            k += 1
        else:
            u.append(k)
            k = 0
        y = (y + 1) % n
    if k != 0:
        u.append(k)
    s = 0
    for i in range(len(u)):
        s += max(0, u[i] - n // 2 + 1)
    print(s)
