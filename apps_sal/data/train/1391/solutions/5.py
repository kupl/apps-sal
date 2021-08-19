# cook your dish here
from collections import defaultdict

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    d = defaultdict(list)
    for i in range(n):
        s, f, p = list(map(int, input().split()))
        d[p].append([s, f])

    ans = 0
    for i in d:
        if len(d[i]) == 1:
            ans += 1

        else:
            d[i].sort(key=lambda x: x[1])
            t = 0
            for j in range(len(d[i])):
                if d[i][j][0] >= t:
                    ans += 1
                    t = d[i][j][1]
    print(ans)
