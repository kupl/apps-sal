def R():
    return map(int, input().split())


n = int(input())
a = list(R())
q = int(input())
p = []
ax = [-1] * n
for _ in range(q):
    p.append(list(R()))
temp = 0
for i in range(q - 1, -1, -1):
    if p[i][0] == 2:
        temp = max(temp, p[i][1])
    elif ax[p[i][1] - 1] == -1:
        ax[p[i][1] - 1] = max(temp, p[i][2])
for i in range(0, n):
    if ax[i] == -1:
        print(max(temp, a[i]), end=' ')
    else:
        print(ax[i], end=' ')
