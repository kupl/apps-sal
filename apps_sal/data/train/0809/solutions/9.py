try:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = []
    for i in range(n - 2):
        a = []
        if l[i] + l[i + 1] > l[i + 2]:
            a.append(l[i])
            a.append(l[i + 1])
            a.append(l[i + 2])
            ans.append(a)
    if len(ans) != 0:
        s = []
        for j in ans:
            s.append(sum(j))
        m = s.index(max(s))
        print('YES')
        for i in reversed(ans[m]):
            print(i, end=' ')
    else:
        print('NO')
except:
    pass
