val = int(input())
for i in range(val):
    (x1, x2, x3, v1, v2) = input().split()
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    v1 = int(v1)
    v2 = int(v2)
    s1 = abs(x3 - x1)
    t1 = s1 / v1
    s2 = abs(x3 - x2)
    t2 = s2 / v2
    if t1 > t2:
        print('Kefa')
    elif t1 < t2:
        print('Chef')
    elif t1 == t2:
        print('Draw')
