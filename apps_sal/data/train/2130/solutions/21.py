ans, col, mod = 1, 0, 1000000007
C = [[1 if i <= j else 0 for i in range(1001)] for j in range(1001)]
for i in range(1, 1001):
    for j in range(1, i + 1):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod
for _ in range(int(input())):
    a = int(input())
    ans *= C[col + a - 1][col]
    ans %= mod
    col += a
print(ans)
