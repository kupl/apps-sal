for t in range(eval(input())):
    n = eval(input())
    a = [[] for i in range(n + 1)]
    for i in range(n - 1):
        (x, y) = list(map(int, input().split()))
        a[x].append(y)
        a[y].append(x)
    vis = [0] * (n + 1)
    vis[1] = 1
    ans = [1]
    t1 = [1]
    t2 = []
    while len(t1) > 0:
        for u in t1:
            for x in a[u]:
                if vis[x] == 0:
                    vis[x] = 1
                    t2.append(x)
        if len(t2) > 1:
            ans.append(t2[0])
            ans.append(t2[-1])
        if len(t2) == 1:
            ans.append(t2[0])
        t1 = t2
        t2 = []
    for x in sorted(ans):
        print(x, end=' ')
    print('')
