k = int(input())
res, mod, last = 1, 10**9 + 7, int(input())
comb = [[0] * 1001 for _ in range(1001)]
comb[0][0] = 1
for i in range(1, 1001):
    comb[i][0] = 1
    for j in range(1, i + 1):
        comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
for _ in range(k - 1):
    to_place = int(input())
    res = (res * comb[last + to_place - 1][to_place - 1]) % mod
    last += to_place
print(res)
