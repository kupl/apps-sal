n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = [0] * n
for i in range(n):
    for j in range(n):
        if j != i:
            ans[i] |= a[i][j]
    print(ans[i], end=' ')
