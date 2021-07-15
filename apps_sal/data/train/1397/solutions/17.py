from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    r = defaultdict(list)
    for i in range(n):
        r[s[i]].append(i)
    t = sorted(r.keys())
    N = len(t)
    l = r[t[0]][0]
    ans = 1
    for i in range(1, N):
        flag = 0
        for j in r[t[i]]:
            if j >= l:
                l = j
                flag = 1
                break
        if flag == 0:
            ans += 1
            l = r[t[i]][0]
    print(ans)

