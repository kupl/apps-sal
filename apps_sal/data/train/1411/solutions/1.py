t = int(input())
k = 0
for i in range(0, t):
    (x, r, a, b) = map(int, input().split(' '))
    if a < b:
        c = r / b
        d = c * (b - a)
        e = d * x
        f = int(e / r)
        g = e % r
        if g == 0:
            print(f - 1)
        else:
            print(f)
    else:
        c = r / a
        d = c * (a - b)
        e = d * x
        f = int(e / r)
        g = e % r
        if g == 0:
            print(f - 1)
        else:
            print(f)
