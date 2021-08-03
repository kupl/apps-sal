n, p, k = list(map(int, input().split()))
pairs = {}
count = 0
for i in map(int, input().split()):
    t = (i**4 - k * i) % p
    if t in pairs:
        count = count + pairs[t]
        pairs[t] += 1

    else:
        pairs[t] = 1

print(count)
