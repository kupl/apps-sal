N, T = list(map(int, input().split()))
towns = list(map(int, input().split()))

p = towns[-1]
r = []

for i in reversed(list(range(N))):
    if towns[i] >= p:
        p = towns[i]
    else:
        r.append(p - towns[i])

res = r.count(max(r))
print(res)
