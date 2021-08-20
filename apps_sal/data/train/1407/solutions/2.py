def fill_grid_max():
    A = [[0 for j in range(50)] for i in range(50)]
    B = [[1, 1, 2, 2], [3, 3, 4, 4], [2, 2, 1, 1], [4, 4, 3, 3]]
    for i in range(50):
        for j in range(50):
            A[i][j] = B[i % 4][j % 4]
    return A


def calculate_k(A):
    k = 0
    for row in A:
        k = max(k, max(row))
    return k


def print_output(A, k, n, m):
    print(k)
    for i in range(n):
        for j in range(m):
            print(A[i][j], end=' ')
        print()


t = int(input())
A = fill_grid_max()
for test in range(t):
    (n, m) = map(int, input().split())
    if n == 1 and m == 1:
        print(1)
        print(1)
    elif n == 1:
        B = A[0][:m]
        k = max(B)
        print(k)
        for x in B:
            print(x, end=' ')
        print()
    elif m == 1:
        B = [[] for x in range(n)]
        for i in range(n):
            B[i].append(A[0][i])
        k = max(A[0][:n])
        print_output(B, k, n, m)
    elif n == 2 and m == 2:
        k = 2
        B = [[1, 1], [2, 2]]
        print_output(B, k, n, m)
    elif n == 2:
        k = 3
        B = [[0 for x in range(m)] for y in range(n)]
        C = [[1, 2, 3], [1, 2, 3]]
        for i in range(n):
            for j in range(m):
                B[i][j] = C[i][j % 3]
        print_output(B, k, n, m)
    elif m == 2:
        k = 3
        B = [[0 for x in range(m)] for y in range(n)]
        C = [[1, 1], [2, 2], [3, 3]]
        for i in range(n):
            for j in range(m):
                B[i][j] = C[i % 3][j]
        print_output(B, k, n, m)
    if n >= 3 and m >= 3:
        print_output(A, 4, n, m)
