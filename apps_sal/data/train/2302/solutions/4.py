N, D = list(map(int, input().split()))
d = list(map(int, input().split()))

dp = [D] * N

if abs(D - d[0]) < D:
    dp[0] = abs(D - d[0])

for i in range(1, N):
    dp[i] = min(dp[i - 1], abs(dp[i - 1] - d[i]))

ans = ["NO"] * N
data = [0] * (N + 1)
for i in range(N - 1, 0, -1):
    if d[i] // 2 > data[i + 1]:
        data[i] = data[i + 1]
    else:
        data[i] = data[i + 1] + d[i]
    if dp[i - 1] > data[i + 1]:
        ans[i] = "YES"

i = 0
if d[i] // 2 > data[i + 1]:
    data[i] = data[i + 1]
else:
    data[i] = data[i + 1] + d[i]

if D > data[i + 1]:
    ans[i] = "YES"

Q = int(input())
q = list(map(int, input().split()))
for i in range(Q):
    print((ans[q[i] - 1]))


# print(dp)
# print(data)
# print(ans)
