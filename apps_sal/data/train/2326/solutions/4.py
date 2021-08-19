from bisect import bisect_left
n = int(input())
alst = list(map(int, input().split()))
lst = list(set(alst))
lst.sort()
blst = []
for a in alst:
    blst.append(bisect_left(lst, a))
imos = [0 for _ in range(len(lst) + 10)]
for b in blst:
    imos[0] += 1
    imos[b + 1] -= 1
for i in range(1, len(lst) + 10):
    imos[i] += imos[i - 1]
bef = 0
for b in blst:
    if b < bef:
        print(0)
        continue
    total = 0
    while bef <= b:
        if bef == 0:
            total += imos[bef] * lst[bef]
        else:
            total += imos[bef] * (lst[bef] - lst[bef - 1])
        bef += 1
    print(total)
