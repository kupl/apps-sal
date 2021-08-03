# cook your dish here

for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    A = [[1], [0]]
    for i in range(1, n + 1):
        A[0].append(k * A[1][i - 1])
        A[1].append(A[0][i - 1] + (k - 1) * A[1][i - 1])
    print(A[0][n] % (10**9 + 7))
