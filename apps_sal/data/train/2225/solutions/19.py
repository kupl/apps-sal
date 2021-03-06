import random
(N, L) = list(map(int, input().split()))
M = 2 * 10 ** 5 + 1
sets = [set() for _ in range(M + 1)]
MOD = 282525872416376072492401
r_max = 10 ** 6
inv_t = [0, 1]
for i in range(2, r_max + 1):
    inv_t.append(inv_t[MOD % i] * (MOD - MOD // i) % MOD)
r = random.randint(10 ** 5, r_max)
rinv = inv_t[r]


def has(s):
    ans = 0
    i = 0
    for x in s:
        ans *= r
        ans += int(x) + (i + 1) ** 2
        ans %= MOD
        i += 1
    return ans % MOD


def tract(x, s, l):
    return (x - int(s) - l ** 2) * rinv % MOD


strs = []
dic = {}
ct = 0
for i in range(N):
    s = input()
    strs.append(s)
    sets[len(s)].add(has(s))
    if has(s) in dic:
        print(('warning!!', s))
        ct += 1
    dic[has(s)] = i
free_num = [0 for _ in range(M + 1)]
for l in range(M, 0, -1):
    while len(sets[l]) > 0:
        x = sets[l].pop()
        last = strs[dic[x]][l - 1]
        x_p = tract(x, last, l)
        sets[l - 1].add(x_p)
        dic[x_p] = dic[x]
        x_anti = (x_p * r + 1 - int(last) + l ** 2) % MOD
        if x_anti in sets[l]:
            sets[l].remove(x_anti)
        else:
            free_num[l] += 1
Grandy = 0
for i in range(M + 1):
    G_base = L - i + 1
    if free_num[i] % 2 == 1:
        Grandy ^= G_base & -G_base
print('Alice' if Grandy > 0 else 'Bob')
