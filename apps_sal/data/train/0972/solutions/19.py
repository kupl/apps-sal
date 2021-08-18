l = list(map(int, input().split()))
n = l[0]
k = l[1]
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
res = []
min = l[-1]
for i in range(n - k):
    x = l[i:i + k]
    if (x[-1] - x[0]) < min:
        min = x[-1] - x[0]
        res = x[:]
print(min)
