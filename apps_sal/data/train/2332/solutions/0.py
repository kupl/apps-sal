from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
for testcaess in range(t):
    n, m, a, b = list(map(int, input().split()))
    E = [[] for i in range(n + 1)]

    for i in range(m):
        x, y = list(map(int, input().split()))
        E[x].append(y)
        E[y].append(x)

    USE1 = [0] * (n + 1)

    Q = deque()
    Q.append(a)

    USE1[a] = 1

    while Q:
        x = Q.pop()

        for to in E[x]:
            if to == b:
                continue
            if USE1[to] == 0:
                USE1[to] = 1
                Q.append(to)

    USE2 = [0] * (n + 1)

    Q = deque()
    Q.append(b)

    USE2[b] = 1

    while Q:
        x = Q.pop()

        for to in E[x]:
            if to == a:
                continue
            if USE2[to] == 0:
                USE2[to] = 1
                Q.append(to)

    ANS1 = 0
    ANS2 = 0

    for i in range(n + 1):
        if i == a or i == b:
            continue
        if USE1[i] == 1 and USE2[i] == 0:
            ANS1 += 1
        elif USE1[i] == 0 and USE2[i] == 1:
            ANS2 += 1

    print(ANS1 * ANS2)
