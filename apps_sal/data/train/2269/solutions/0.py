from collections import deque

N, M = list(map(int, input().split()))
adj = [[1 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a][b] = 0
    adj[b][a] = 0
adj_inv = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if adj[i][j] == 1:
            adj_inv[i].append(j)
            adj_inv[j].append(i)

seen = [0] * (N + 1)
num = []
for i in range(1, N + 1):
    if seen[i] == 0:
        plus = 0
        minus = 0
        que = deque()
        que.append(i)
        seen[i] = 1
        plus += 1
        while que:
            v = que.pop()
            u_list = adj_inv[v]
            for u in u_list:
                if seen[u] == 0:
                    que.append(u)
                    seen[u] = -seen[v]
                    if seen[u] == 1:
                        plus += 1
                    else:
                        minus += 1
                else:
                    if seen[u] == seen[v]:
                        print((-1))
                        return
        num.append((min(plus, minus), max(plus, minus)))

min_sum = 0
add = []
for i in range(len(num)):
    min_sum += num[i][0]
    add.append(num[i][1] - num[i][0])

dp = [[0 for _ in range((N // 2) + 1)] for _ in range(len(add) + 1)]
dp[0][min_sum] = 1
for i in range(len(add)):
    for j in range(min_sum, (N // 2) + 1):
        if dp[i][j] == 1:
            if j + add[i] <= (N // 2):
                dp[i + 1][j + add[i]] = 1
            dp[i + 1][j] = 1

dp_last = dp[-1]
for i in range(len(dp_last) - 1, -1, -1):
    if dp_last[i] == 1:
        N1 = i
        break

print(((N1 * (N1 - 1)) // 2 + ((N - N1) * (N - N1 - 1)) // 2))
