s = int(input())
MOD = int(1000000000.0 + 7)
comb = [[1] + [0 for i in range(1000)] for j in range(1001)]
for i in range(1, 1001):
    for j in range(1, i + 1):
        comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD
res = 1
sums = 0
for i in range(s):
    x = int(input())
    res = res * comb[sums + x - 1][x - 1] % MOD
    sums += x
print(res)
