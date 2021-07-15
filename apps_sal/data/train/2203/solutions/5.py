3

def remove(A, i, n):
    for j in range(n):
        A[i][j] = 0
        A[j][i] = 0


n = int(input())
A = [list(map(int, input().split())) for i in range(n)]

ans = [0 for i in range(n)]
for i in range(n - 1):
    t = -1
    for j in range(n):
        f = True
        g = False
        for k in range(n):
            if not (A[j][k] in (0, i + 1) and A[k][j] in (0, i + 1)):
                f = False
            if A[j][k] != 0:
                g = True
        if f and g:
            t = j


    ans[t] = i + 1
    remove(A, t, n)


for i in range(n):
    if ans[i] == 0:
        ans[i] = n

print(" ".join(map(str, ans)))
                

