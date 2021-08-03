from operator import itemgetter
n = int(input().strip())
ans = 0
l = []
for i in range(n):
    l.append([int(x) for x in input().strip().split()])

l.sort(key=itemgetter(1))
x = l[0][1]
y = 1
for i in range(1, len(l)):
    if l[i][1] != x:
        ans = ans + (y * (y - 1)) // 2
        x = l[i][1]
        y = 1
    else:
        y = y + 1
ans = ans + (y * (y - 1)) // 2

l.sort()
x = l[0][0]
y = 1
for i in range(1, len(l)):
    if l[i][0] != x:
        ans = ans + (y * (y - 1)) // 2
        x = l[i][0]
        y = 1
    else:
        y = y + 1
ans = ans + (y * (y - 1)) // 2

x0, x1 = l[0][0], l[0][1]
y = 1
for i in range(1, len(l)):
    if l[i][0] != x0 or l[i][1] != x1:
        ans = ans - (y * (y - 1)) // 2
        x0, x1 = l[i][0], l[i][1]
        y = 1
    else:
        y = y + 1
ans = ans - (y * (y - 1)) // 2

print(ans)
