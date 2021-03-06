import collections
import bisect
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = collections.defaultdict(list)
    (c, find, ans, l) = (0, 0, 0, [])
    for i in range(n):
        if a[i] not in d:
            l.append(a[i])
            c += 1
        d[a[i]].append(i)
    l.sort()
    for i in range(c):
        if i == 0:
            ans += 1
            find = d[l[i]][0] + 1
        else:
            k = bisect.bisect_left(d[l[i]], find)
            if k == 0:
                find = d[l[i]][k] + 1
            elif k == len(d[l[i]]):
                find = d[l[i]][0] + 1
                ans += 1
            else:
                find = d[l[i]][k] + 1
    print(ans)
