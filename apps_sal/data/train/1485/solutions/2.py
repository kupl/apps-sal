def row(alist):
    (a, n) = (0, len(alist))
    for i in range(n // 2):
        if alist[i] == '1':
            a += 1
    for i in range(n // 2, n):
        if alist[i] == '1':
            a -= 1
    return a


t = int(input())
for count in range(t):
    n = int(input())
    mat = [input() for i in range(n)]
    A = []
    for i in range(n):
        A.append(row(mat[i]))
    s = sum(A)
    B = [abs(s)]
    if s > 0:
        for i in range(n):
            if A[i] > 0:
                B.append(abs(s - 2 * A[i]))
    else:
        for i in range(n):
            if A[i] < 0:
                B.append(abs(s - 2 * A[i]))
    print(min(B))
