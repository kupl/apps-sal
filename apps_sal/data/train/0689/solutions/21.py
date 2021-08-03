def fun(t):
    s = []
    a = []
    b = []
    for _ in range(t):
        x, y = list(map(int, input().split()))
        s.append(x + y)
        a.append(x)
        b.append(y)

    for i in range(t):
        if(s[i] in a):
            yy = a.index(s[i])
            xx = a[yy] + b[yy]
            if(xx == a[i]):
                return "YES"
    return "NO"


t = int(input())
print(fun(t))
