# cook your dish here
T = int(input())
mat = []
for _ in range(T):
    a = list(map(int, input().split()))
    mat.append(a)
f = 0
for i in range(T):
    ch = mat[i][0] + mat[i][1]
    for j in range(T):
        if ch == mat[j][0] and mat[i][0] == mat[j][0] + mat[j][1]:
            f = 1
            break
if f:
    print('YES')
else:
    print('NO')
