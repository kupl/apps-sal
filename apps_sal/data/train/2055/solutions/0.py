MOD = 10 ** 9 + 7
s = input()
n = int(input())
qs = [['', s]] + [input().split('->') for i in range(n)]
ds = {}
for i in range(10):
    ds[str(i)] = (10, i)
for i in range(n, -1, -1):
    out = 0
    mul = 1
    for d in qs[i][1]:
        out = (out * ds[d][0] + ds[d][1]) % MOD
        mul = mul * ds[d][0] % MOD
    ds[qs[i][0]] = (mul, out)
print(ds[''][1])
