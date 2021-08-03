n = int(input())
l = list(map(int, input().split()))
d = l.copy()
d.append(0)
for i in range(2, n + 1):
    mini = min(d[i - 1], d[i - 2])
    d[i] += mini
if(d[-1] == d[-2]):
    print(d[-1])
else:
    f = l.copy()
    f.append(0)
    c = l[0]
    for i in range(3, n + 1):
        mini = min(f[i - 1], f[i - 2])
        f[i] += mini
    if(f[-1] == f[-3]):
        print(f[-1] + c)
    else:
        print(d[-1])
