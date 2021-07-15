n = int(input())
a = []
s = 0
for i in range (n):
    a.append(input())
for i in range(7):
    tmp = 0
    for e in range(n):
        tmp += int(a[e][i])
    if tmp > s:
        s = tmp
print(s)
