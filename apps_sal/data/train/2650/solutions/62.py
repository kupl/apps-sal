N, L = map(int, input().split())
mat = []
for i in range(N):
    mat.append(input())
while i <= N:
    FINISH = 0
    for i in range(N - 1):
        if mat[i] > mat[i + 1]:
            tmp = mat[i]
            mat[i] = mat[i + 1]
            mat[i + 1] = tmp
            FINISH += 1
    if FINISH == 0:
        break
for i in range(N):
    print(mat[i], end="")
