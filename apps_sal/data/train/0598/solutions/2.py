n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

if k == 0:
    ans = a
else:
    t = max(a)
    for i in range(n):
        a[i] = t - a[i]

    if k % 2 == 0:
        t = max(a)
        for i in range(n):
            a[i] = t - a[i]

for i in a:
    print(i, end=' ')

print()
