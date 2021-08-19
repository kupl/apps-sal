import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, a, b, da, db = list(map(int, input().split()))
    EDGE = [[] for i in range(n + 1)]

    for i in range(n - 1):
        x, y = list(map(int, input().split()))
        EDGE[x].append(y)
        EDGE[y].append(x)

    if db <= da * 2:
        print("Alice")
        continue

    Q = [a]
    USE = [-1] * (n + 1)
    USE[a] = 0

    while Q:
        x = Q.pop()
        for to in EDGE[x]:
            if USE[to] == -1:
                USE[to] = USE[x] + 1
                Q.append(to)

    # print(USE)

    if USE[b] <= da:
        print("Alice")
        continue

    MAX = -1
    MAXIND = -1
    for i in range(1, n + 1):
        if USE[i] > MAX:
            MAX = USE[i]
            MAXIND = i

    Q = [MAXIND]
    USE2 = [-1] * (n + 1)
    USE2[MAXIND] = 0

    while Q:

        x = Q.pop()
        for to in EDGE[x]:
            if USE2[to] == -1:

                USE2[to] = USE2[x] + 1
                Q.append(to)

    DIA = max(USE2)
    # print(MAXIND,USE2,DIA)

    if DIA <= da * 2:
        print("Alice")
        continue

    else:
        print("Bob")
