(n, t) = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for i in range(n)]
b[n - 1] = a[n - 1]
for i in range(n - 1):
    b[n - i - 2] = max(b[n - i - 1], a[n - i - 2])
samax = 0
maxkai = 0
for i in range(n - 1):
    if b[i + 1] - a[i] > samax:
        maxkai = 1
        samax = b[i + 1] - a[i]
    elif b[i + 1] - a[i] == samax:
        maxkai += 1
print(maxkai)
