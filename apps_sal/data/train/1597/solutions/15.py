import math


def search(l):
    a = l[0]
    n = l[1]
    g = []
    r = []
    e = []
    t = []
    z = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                g.append(i)
            else:
                g.append(i)
                g.append(int(n / i))
        i = i + 1
    g.sort()
    for i in g:
        k = int(n / i) - 1
        e.append(k)
    for j in e:
        if j % a == 0:
            p = int(j / a)
            ind = e.index(j)
            f = g[ind] * p
            z.append(f)
            t.append(p)
    z.sort()
    if len(z) == 1 and z[0] == 0:
        print('0')
    else:
        z.remove(0)
        print(len(z))
        print(*z, sep=' ')


t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    search(l)
