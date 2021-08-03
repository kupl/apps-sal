t = int(input())
while t:
    t -= 1
    n = int(input())
    d = dict()
    for i in range(n):
        x, y = map(int, input().split())
        f = d.get(x)
        if f == None:
            d[x] = y
        else:
            d[x] = max(d[x], y)
    z = sorted(d.values())[::-1]
    l = len(z)
    if l < 3:
        print(0)
    else:
        print(z[0] + z[1] + z[2])
