from collections import Counter
n = int(input())
pref = [0]
app = pref.append
for (i, x) in enumerate(map(int, input().split())):
    app(pref[-1] ^ x)
d = Counter(pref[::2])
di = Counter(pref[1::2])
res = 0
for (i, x) in enumerate(d.values()):
    res += x * (x - 1) // 2
for (i, x) in enumerate(di.values()):
    res += x * (x - 1) // 2
print(res)
