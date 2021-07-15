MOD = 10 ** 9 + 7
s, t = input(), input()

p = t + '#' + s
z = [0] * len(p)
l = r = 0
for i in range(1, len(p)):
    if i <= r:
        z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < len(p) and p[z[i]] == p[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
        l, r = i, i + z[i] - 1

f = [0] * (len(p) + 1)
fsum = [0] * (len(p) + 1)
fsum2 = [0] * (len(p) + 1)
for i in range(len(p) - 1, len(t), -1):
    if z[i] == len(t):
        f[i] = fsum2[i + z[i]] + len(p) - i - z[i] + 1
    else:
        f[i] = f[i + 1]
    fsum[i] = (fsum[i + 1] + f[i]) % MOD
    fsum2[i] = (fsum2[i + 1] + fsum[i]) % MOD
print(fsum[len(t) + 1])

