t = int(input())
for i in range(t):
    n = int(input())
    hash = {}
    l = list(map(int, input().split()))
    for j in range(n):
        try:
            hash[l[j]]
        except:
            hash[l[j]] = 1
        else:
            hash[l[j]] += 1
    flag = 0
    max = 0
    for j in range(n):
        if hash[l[j]] > n // 2:
            flag = 1
            break
        elif hash[l[j]] > max:
            max = hash[l[j]]
    v = sorted(range(len(l)), key=lambda k: l[k])
    u = sorted(l)
    ans = [0] * n
    if flag == 0:
        print('Yes')
        z = u[max:] + u[:max]
        for i in range(n):
            ans[v[i]] = z[i]
        print(*ans)
    else:
        print('No')
