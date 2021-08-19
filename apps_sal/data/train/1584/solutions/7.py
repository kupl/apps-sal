# cook your dish here
r, c, n = map(int, input().split())
x = {}
y = {}
xy = {}
for i in range(n):
    a = [int(i) for i in input().split()]
    if x.get(a[0]) == None:
        x[a[0]] = 1
    else:
        x[a[0]] += 1
    if y.get(a[1]) == None:
        y[a[1]] = 1
    else:
        y[a[1]] += 1
    xy[tuple(a)] = 1
xmax = max(x, key=x.get)
ymax = max(y, key=y.get)
ar = []
ar.append(xmax)
ar.append(ymax)
count = x[xmax] + y[ymax]
if xy.get(tuple(ar)) != None:
    count -= 1
print(count)
