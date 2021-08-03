n, k = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
m = 10000000000000000000000000000000
for i in range(n - k + 1):
    m = min(m, l[i + k - 1] - l[i])
print(m)
