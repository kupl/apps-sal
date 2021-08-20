n = int(input())
n -= 1
l = list(map(int, input().split()))
x = int(input())
c = 0
m = 0
z = 0
i = 0
l.sort()
while i < n:
    if l[i] <= x:
        c += 1
        x = x - l[i]
        i += 1
    elif c >= 1:
        c -= 1
        x = x + l[n]
        n -= 1
    if m < c:
        m = c
print(m)
