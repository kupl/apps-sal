n, m = list(map(int, input().split()))
gym = [[0 for i in range(m + 1)]]
for row in range(n):
    gym.append([0] + list(map(int, input().split())))

bToMid = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        bToMid[i][j] = gym[i][j] + max(bToMid[i - 1][j], bToMid[i][j - 1])
bToEnd = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        bToEnd[i][j] = gym[i][j] + max(bToEnd[i + 1][j], bToEnd[i][j + 1])
aToMid = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(n, 0, -1):
    for j in range(1, m + 1):
        aToMid[i][j] = gym[i][j] + max(aToMid[i + 1][j], aToMid[i][j - 1])
aToEnd = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(m, 0, -1):
        aToEnd[i][j] = gym[i][j] + max(aToEnd[i - 1][j], aToEnd[i][j + 1])
#print(bToMid[1][2], bToEnd[3][2], aToMid[2][1], aToEnd[2][3])
best = 0
bestIJ = ()
for i in range(2, n):
    for j in range(2, m):
        best = max(best, bToMid[i][j - 1] + bToEnd[i][j + 1] + aToMid[i + 1][j] + aToEnd[i - 1][j])
        best = max(best, bToMid[i - 1][j] + bToEnd[i + 1][j] + aToMid[i][j - 1] + aToEnd[i][j + 1])
        bestIJ = (i, j)
print(best)
# print(bestIJ)
