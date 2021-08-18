from collections import defaultdict
from operator import itemgetter
for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    for i in range(n):
        x, y = map(int, input().split())
        if not d[x]:
            d[x].append(y)
        else:
            d[x][0] = max(d[x][0], y)

    l = sorted(d.items(), key=itemgetter(1))[::-1]
    try:
        print(sum(l[0][1] + l[1][1] + l[2][1]))
    except:
        print(0)
