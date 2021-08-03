n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = [0] * 100006
maximum = 0
prev = [0] * 100006
prev[0] = b[0]
for j in range(n):
    prev[j] = b[j] + prev[j - 1]
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            maximum = max(maximum, a[i])
        elif i < j:
            maximum = max(maximum, a[i] + a[j] + prev[j - 1] - prev[i])
        else:
            maximum = max(maximum, a[i] + a[j] + prev[n - 1] + prev[j - 1] - prev[i])
print(maximum)
