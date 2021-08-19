(n, k) = [int(s) for s in input().split()]
s = n - k
t = 0
if (s - 1) % k == 1:
    t = 1
if (s - 1) % k >= 2:
    t = 2
print(2 * ((s - 1) // k) + t + 2)
for i in range(n // k):
    for j in range(k):
        if 1 + j + (i + 1) * k <= n:
            print(1 + j + i * k, 1 + j + (i + 1) * k)
        elif 1 + j + i * k < n:
            print(1 + j + i * k, n)
for i in range(1, n % k):
    print(n - i, n)
