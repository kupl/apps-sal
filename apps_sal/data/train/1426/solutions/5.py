t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    flav = list(map(int, input().split()))
    ans = []
    res = 0
    k = 0
    for i in range(n):
        (d, f, b) = map(int, input().split())
        if flav[d - 1] == 0:
            res += b
            ans.append(-1)
            k += 1
        else:
            flav[d - 1] -= 1
            res += f
            ans.append(d)
    l = []
    for i in range(m):
        while flav[i] != 0 and k != 0:
            flav[i] -= 1
            k -= 1
            l.append(i + 1)
    print(res)
    c = 0
    for i in range(n):
        if ans[i] == -1:
            print(l[c], end=' ')
            c += 1
        else:
            print(ans[i], end=' ')
    print()
