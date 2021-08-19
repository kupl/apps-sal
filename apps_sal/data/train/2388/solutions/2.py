import sys
from collections import deque
for _ in range(int(input())):
    (n, m) = list(map(int, sys.stdin.readline().split()))
    a = [[] for i in range(n + 1)]
    for i in range(m):
        (x, y) = list(map(int, sys.stdin.readline().split()))
        a[x].append(y)
        a[y].append(x)
    col = [-1] * (n + 1)
    col[1] = 1
    d = deque([1])
    vis = [0] * (n + 1)
    ans = [[], [1]]
    while d:
        p = d.popleft()
        for i in a[p]:
            if col[i] == -1:
                col[i] = 1 - col[p]
                ans[1 - col[p]].append(i)
                d.append(i)
    if len(ans[0]) <= n // 2:
        print(len(ans[0]))
        print(*ans[0])
    else:
        print(len(ans[1]))
        print(*ans[1])
