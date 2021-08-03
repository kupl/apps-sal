def valid(x, y, m, n):
    if 0 <= x < m and 0 <= y < n:
        return 1
    return 0


def neigh(A, x, y, m, n):
    B = []
    if valid(x, y - 2, m, n):
        B.append(A[x][y - 2])
    if valid(x - 2, y, m, n):
        B.append(A[x - 2][y])
    if valid(x - 1, y - 1, m, n):
        B.append(A[x - 1][y - 1])
    if valid(x - 1, y + 1, m, n):
        B.append(A[x - 1][y + 1])
    return set(B)


AA = [[1, 1, 2, 2], [1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3], [1, 2, 2, 1], [1, 2, 3, 1], [1, 2, 3, 4]]
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    if m >= 3 and n >= 3:
        P = set(range(1, 5))
    elif m == 1 and n == 1:
        P = set(range(1, 2))
    elif m + n == 3:
        P = set(range(1, 2))
    elif m == 1 or n == 1:
        P = set(range(1, 3))
    elif m == 2 and n == 2:
        P = set(range(1, 3))
    elif m == 2 or n == 2:
        P = set(range(1, 4))
    A = [[0 for j in range(n)] for k in range(m)]
    pk = 0
    if m == 1:
        A[0][0] = 1
        for j in range(1, n):
            B = neigh(A, 0, j, m, n)
            A[0][j] = min(P - B)
        print(max(P))
        for j in A[0]:
            print(j, end=" ")
        print()
        continue
    while True:
        trig = 0
        if max(P) == 4:
            for j in range(n):
                A[0][j] = AA[pk][j % 4]
        else:
            for j in range(n):
                A[0][j] = (j % max(P)) + 1
        for j in range(1, m):
            for k in range(n):
                B = neigh(A, j, k, m, n)
                if P - B == set():
                    trig = 1
                    break
                A[j][k] = min(P - B)
            if trig == 1:
                pk += 1
                A = [[0 for j in range(n)] for k in range(m)]
                break
        else:
            break
    print(max(P))
    for j in A:
        for k in j:
            print(k, end=" ")
        print()
