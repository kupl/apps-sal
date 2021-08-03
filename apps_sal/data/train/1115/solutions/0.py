T = int(input())

M = 10 ** 9 + 7

for _ in range(T):
    N = int(input())

    A = list(map(int, input().split()))

    if N == 1:
        print(0)
        continue

    B = {}
    C = {}

    for i in range(N - 1):
        u, v = input().split()
        u = int(u) - 1
        v = int(v) - 1

        if u not in B:
            B[u] = []

        if v not in B:
            B[v] = []

        B[u].append(v)
        B[v].append(u)

    total_leaves = 0

    for i in B:
        if len(B[i]) == 1:
            total_leaves += 1

    S = [0]

    visited = [False] * N

    parent = [-1] * N

    total_visits = [0] * N

    while len(S) > 0:
        current = S.pop(len(S) - 1)

        if visited[current]:
            p = parent[current]
            if p != -1:
                total_visits[p] += total_visits[current]
                if p not in C:
                    C[p] = {}
                C[p][current] = total_visits[current]
                if current not in C:
                    C[current] = {}
                C[current][p] = total_leaves - C[p][current]
        else:
            S.append(current)
            visited[current] = True
            for i, j in enumerate(B[current]):
                if not visited[j]:
                    parent[j] = current
                    S.append(j)
            if len(B[current]) == 1:
                total_visits[current] = 1
                p = parent[current]
                if p != -1:
                    if p not in C:
                        C[p] = {}
                    C[p][current] = 1

    D = {}
    for i in C:
        sum1 = 0
        for j in C[i]:
            sum1 += C[i][j]
        D[i] = sum1

    E = [0] * N
    for i in C:
        sum1 = 0
        for j in C[i]:
            D[i] -= C[i][j]
            sum1 += C[i][j] * D[i]
        E[i] = sum1

    for i, j in enumerate(E):
        if j == 0:
            for k in C[i]:
                E[i] = C[i][k]

    E.sort()
    E.reverse()
    A.sort()
    A.reverse()

    E = [x % M for x in E]
    A = [x % M for x in A]

    ans = 0
    for i, j in zip(E, A):
        a = i * j
        a %= M
        ans += a
        ans %= M

    print(ans)
