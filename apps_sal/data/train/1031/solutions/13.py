import math
try:
    t = eval(input())
except EOFError:
    t = 0
while(t):
    try:
        h, s = list(map(int, input().split()))
    except EOFError:
        h = 0
        s = 0
    z = (h**4) - (4 * (4 * (s**2)))
    if(z < 0):
        print(-1)
    else:
        z = math.sqrt(z)
        z = (h**2) + z
        z = z / 2
        z = math.sqrt(z)
        y = 2 * s
        try:
            y = y / z
        except ZeroDivisionError:
            y = 0
        if(z > y):
            a = y
            b = z
        else:
            a = z
            b = y
        h = h * 1.0
        print(a, b, h)
    t = t - 1
