n, k = input().split()
n = int(n)
k = int(k)
l = [0] * n
for x in range(n):
    l[x] = int(input())
l.sort()
c = 0
i = 0
while i < n - 1:
    if l[i + 1] - l[i] <= k:
        i += 1
        c += 1
    i += 1
print(c)
