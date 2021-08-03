from array import *

n = int(input())
Becone = [list(map(int, input().split())) for i in range(n)]
Becone.sort(key=lambda x: x[0])
dp = array('i', [0] * 1000001)

if Becone[0][0] == 0:
    dp[0] = 1
    Becone.pop(0)

ans = n - dp[0]
for i in range(1, 1000001):
    if not Becone:
        break
    if i != Becone[0][0]:
        dp[i] = dp[i - 1]
        continue

    a, b = Becone.pop(0)
    if a - b <= 0:
        dp[i] = 1
    else:
        dp[i] = dp[i - b - 1] + 1

    ans = min(ans, n - dp[i])

print(ans)
