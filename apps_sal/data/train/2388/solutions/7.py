from collections import deque
import sys
sys.setrecursionlimit(10 ** 5 + 1)
inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW():
    return sys.stdin.readline().strip()


def RI():
    return int(RW())


def RMI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def RWI():
    return [x for x in sys.stdin.readline().strip().split()]


for _ in range(RI()):
    (n, m) = RMI()
    a = [[] for i in range(n + 1)]
    for i in range(m):
        (x, y) = RMI()
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
                tog = 1 - col[p]
                col[i] = tog
                ans[tog].append(i)
                d.append(i)
    if len(ans[0]) <= n // 2:
        print(len(ans[0]))
        print(*ans[0])
    else:
        print(len(ans[1]))
        print(*ans[1])
