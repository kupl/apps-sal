def modulus(n):
    mod = int(1000000000.0) + 7
    if n < 0:
        n += mod
    else:
        n = n % mod
    return n


(n, k) = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))
freak = []
for i in list(set(array)):
    freak.append(array.count(i))
dp = [[0] * len(freak) for _ in range(k)]
for i in range(len(freak)):
    dp[0][i] = freak[i]
for row in range(1, k):
    for col in range(0, len(freak) - row):
        dp[row][col] = modulus(freak[col] * sum(dp[row - 1][col + 1:]))
ans = 1
for i in dp:
    ans += sum(i)
ans = modulus(ans)
print(ans)
