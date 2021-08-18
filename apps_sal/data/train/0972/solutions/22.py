n, k = list(map(int, input().split()))
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()
m = l[k - 1] - l[0]
for i in range(n - k):
    if(l[k - 1 + i] - l[i] < m):
        m = l[i + k - 1] - l[i]
print(m)
