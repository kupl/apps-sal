n = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(0, n):
    for j in range(0, i):
        a = abs(l[i] - l[j])
        c += a
print(c)
