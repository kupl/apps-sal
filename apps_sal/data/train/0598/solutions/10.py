(n, k) = input().split()
(n, k) = (int(n), int(k))
a = list(map(int, input().split()))
maxi = 0
mini = 0
if k != 0:
    maxi = max(a)
    mini = min(a)
mini = maxi - mini
for i in range(n):
    a[i] = maxi - a[i]
if k % 2 == 0:
    for i in range(n):
        a[i] = mini - a[i]
print(' '.join(map(str, a)))
