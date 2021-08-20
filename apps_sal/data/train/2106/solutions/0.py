(p, n) = ([], int(input()))
a = b = 0
for i in range(n):
    t = list(map(int, input().split()))
    k = t[0] // 2 + 1
    a += sum(t[1:k])
    if t[0] & 1:
        p.append(t[k])
        b += sum(t[k + 1:])
    else:
        b += sum(t[k:])
p.sort(reverse=True)
print(a + sum(p[0::2]), b + sum(p[1::2]))
