n, k = map(int, input().split())
l = []
l.append(-1)
for i in range(n):
    l.append(int(input()))
l.sort()
m = l[k] - l[1]
for i in range(2, n - k):
    if(l[i + k - 1] - l[i] < m):
        m = l[i + k - 1] - l[i]
print(m)
