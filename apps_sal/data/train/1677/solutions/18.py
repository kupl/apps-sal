n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = [0] * 100006
maximum = 0
prev = [0] * 100006
diff = [0] * 100006
summ = [0] * 100006
prev[0] = b[0]
for i in a:
    maximum = max(maximum, i)
for j in range(n):
    prev[j] = b[j] + prev[j - 1]
diff[0] = a[0] - prev[0]
summ[0] = a[0]
for i in range(1, n):
    diff[i] = max(diff[i - 1], a[i] - prev[i])
for i in range(1, n):
    summ[i] = max(summ[i - 1], a[i] + prev[i - 1])
for i in range(1, n):
    maximum = max(maximum, a[i] + prev[i - 1] + diff[i - 1])
for i in range(1, n):
    maximum = max(maximum, a[i] + prev[n - 1] - prev[i] + summ[i - 1])
print(maximum)
