from collections import deque
import sys
input = sys.stdin.readline

Q = int(input())

for q in range(Q):
    n, m = list(map(int, input().split()))

    E = [list(map(int, input().split())) for i in range(m)]

    ELIST = [[] for i in range(n + 1)]
    for a, b in E:
        ELIST[a].append(b)
        ELIST[b].append(a)

    check = [0] * (n + 1)
    ANS = []

    Q = deque([1])
    E2 = [[] for i in range(n + 1)]

    while Q:
        x = Q.pop()
        check[x] = 1
        for to in ELIST[x]:
            if check[to] == 0:
                E2[x].append(to)
                E2[to].append(x)
                check[to] = 1
                Q.append(to)

    # print(E2)
    ELIST = E2

    check = [0] * (n + 1)

    QUE = deque([])
    QUE.append([1, 0])

    while QUE:
        x, point = QUE.pop()
        if point == 0:
            if check[x] == 1:
                continue
            check[x] = 1
            ANS.append(x)

            for to in ELIST[x]:
                if check[to] == 0:
                    check[to] = 1
                    QUE.appendleft([to, 1])

        else:
            for to in ELIST[x]:
                if check[to] == 0:
                    QUE.appendleft([to, 0])

    if len(ANS) <= n // 2:

        print(len(ANS))
        print(*ANS)
        continue

    check = [0] * (n + 1)
    ANS = []

    QUE = deque([])
    QUE.append([ELIST[1][0], 0])

    while QUE:
        x, point = QUE.pop()
        if point == 0:
            if check[x] == 1:
                continue
            check[x] = 1
            ANS.append(x)

            for to in ELIST[x]:
                if check[to] == 0:
                    check[to] = 1
                    QUE.appendleft([to, 1])

        else:
            for to in ELIST[x]:
                if check[to] == 0:
                    QUE.appendleft([to, 0])

    print(len(ANS))
    print(*ANS)
