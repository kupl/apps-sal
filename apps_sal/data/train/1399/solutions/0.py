import numpy as np


def solve(n, k, a, l, r):
    shape = (n, n)
    mat = np.zeros(shape, dtype=np.int64)
    for i in range(n):
        for j in range(l[i], r[i]):
            mat[i][j] = 1

    ans = np.eye(n, n, dtype=np.int64)
    while(k > 0):
        if k % 2 == 1:
            ans = np.matmul(mat, ans)
            ans %= 2
        mat = np.matmul(mat, mat)
        mat %= 2
        k = k // 2
    result = []
    for i in range(n):
        aux = 0
        for j in range(n):
            if ans[i][j] == 1:
                aux ^= a[j]
        result.append(aux)
    return result


t = int(input())
for i in range(t):
    s = input().split()
    n = int(s[0])
    k = int(s[1])
    a = []
    l = []
    r = []
    s = input().split()
    for i in range(n):
        a.append(int(s[i]))
    for i in range(n):
        s = input().split()
        l.append(int(s[0]) - 1)
        r.append(int(s[1]))
    arr = solve(n, k - 1, a, l, r)
    s = ""
    for e in arr:
        s += str(e)
        s += " "
    print(s)
