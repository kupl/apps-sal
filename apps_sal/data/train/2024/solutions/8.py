n = int(input().strip())

p = [0] + list(map(float, input().split()))

a = [0] * (n + 1)
b = [0] * (n + 1)


for i in range(1, n + 1):
    b[i] = (b[i - 1] + 1) * p[i]
    a[i] = (a[i - 1] + 2 * b[i - 1] + 1) * p[i] + a[i - 1] * (1 - p[i])

print(a[-1])
