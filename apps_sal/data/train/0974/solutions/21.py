import math
t = int(input())
while t > 0:
    (a, b, c, d) = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if d == c:
        if a == b:
            print('YES')
        else:
            print('NO')
    else:
        m = (a - b) % (c - d)
        if m == 0:
            print('YES')
        else:
            print('NO')
    t = t - 1
