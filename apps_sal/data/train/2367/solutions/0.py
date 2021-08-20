q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    t = input()
    x = set(s)
    y = set(t)
    if x != y:
        print('NO')
        continue
    if len(x) == n:
        a = [0] * n
        for (i, c) in enumerate(t):
            a[i] = s.find(c)
        yeet = 0
        vis = [False] * n
        for i in range(n):
            if vis[i]:
                continue
            j = i
            cyc = 0
            while not vis[j]:
                cyc += 1
                vis[j] = True
                j = a[j]
            yeet += (cyc - 1) % 2
            yeet %= 2
        if yeet == 0:
            print('YES')
        else:
            print('NO')
        continue
    print('YES')
