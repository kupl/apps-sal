import math

N, D = list(map(int, input().split()))
Ds = list(map(int, input().split()))
Q = int(input())
Qs = list(map(int, input().split()))

dp = [math.inf]*(N+1) # (iから先だけをみて)＝＞ゴールできない最小
dp[-1] = 1
for i in range(N-1, -1, -1):
    if Ds[i] >= 2 * dp[i+1]:
        dp[i] = dp[i+1]
    else:
        dp[i] = dp[i+1]+Ds[i]

Pos = [D]
for i in range(N):
    if Ds[i] > Pos[-1]*2:
        Pos.append(Pos[-1])
    else:
        Pos.append(abs(Pos[-1]-Ds[i]))

for q in Qs:
    if dp[q]>Pos[q-1]:
        print('NO')
    else:
        print('YES')

