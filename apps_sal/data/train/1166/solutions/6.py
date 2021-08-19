n = int(input())
l = list(map(int, input().split()))
d = {}
for i in range(n):
    a = []
    x = l[i]
    for j in range(i, n):
        a.append(l[j])
        x = min(x, l[j])
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
q = int(input())
while q > 0:
    b = int(input())
    if b in d:
        print(d[b])
    else:
        print(0)
    q -= 1
