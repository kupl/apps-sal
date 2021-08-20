n = int(input())
a = list(range(n))
h = list(range(n))
m = 2
for i in range(n):
    (a[i], h[i]) = [int(s) for s in input().split()]
if n < 3:
    m = n
else:
    for j in range(1, n - 1):
        if a[j] - h[j] > a[j - 1]:
            m += 1
        elif a[j] + h[j] < a[j + 1]:
            m += 1
            a[j] = a[j] + h[j]
        else:
            continue
print(m)
