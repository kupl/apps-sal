import sys


def multiply(matrix1, matrix2, mod):
    ans = [[-1 for i in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            s = 0
            k = 0
            while k < len(matrix1[0]):
                s += matrix1[i][k] * matrix2[k][j] % mod
                k += 1
            ans[i][j] = s % mod
    return ans


def power(a, b, mod):
    res = [[1, 0], [0, 1]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = a[i][j] % mod
    while b > 0:
        if b & 1:
            res = multiply(res, a, mod)
        b = b >> 1
        a = multiply(a, a, mod)
    return res


t = int(sys.stdin.readline())
mod = 10 ** 9 + 7
for _ in range(t):
    (n, m) = list(map(int, sys.stdin.readline().split()))
    base = [[m], [0]]
    a = [[m - 1, m - 1], [1, 0]]
    ans = power(a, n - 1, mod)
    ans = multiply(ans, base, mod)
    print((ans[0][0] + ans[1][0]) % mod)
