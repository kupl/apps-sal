xs, yx, xt, yt = map(int, input().split())
N = int(input())
l = [[], [xs, yx, 0], [xt, yt, 0]]
for i in range(N):
    l.append(list(map(int, input().split())))
# 距離リスト
d = [[0] * (N + 3) for _ in range(N + 3)]
for i in range(1, N + 3):
    d[i][i] = 0
# O(10**6)
for i in range(1, N + 3):
    for j in range(i + 1, N + 3):
        sa = (l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2
        kyori = max(0, sa**(1 / 2) - l[i][2] - l[j][2])
        d[i][j] = kyori
        d[j][i] = kyori

md = [float("inf")] * (N + 3)
h = [i for i in range(1, N + 3)]
for i in range(1, N + 3):
    md[i] = d[1][i]
seen = [False] * (N + 3)
seen[1] = True
while True:
    # vを出す
    v = -1
    for i in h:
        if seen[i] == False and v == -1:
            v = i
        elif seen[i] == False and md[i] < md[v]:
            v = i
    if v == -1:
        break
    seen[v] = True
    for j in range(1, N + 3):
        md[j] = min(md[j], md[v] + d[v][j])
print(md[2])
