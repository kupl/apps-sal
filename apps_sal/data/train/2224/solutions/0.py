n = int(input())
a = [int(x) for x in input().strip()]
b = [int(x) for x in input().strip()]
(p, q, r, s) = (0, 0, 0, 0)
for i in range(n):
    if a[i] * 2 + b[i] == 0:
        p += 1
    if a[i] * 2 + b[i] == 1:
        q += 1
    if a[i] * 2 + b[i] == 2:
        r += 1
    if a[i] * 2 + b[i] == 3:
        s += 1
print(p * r + p * s + q * r)
