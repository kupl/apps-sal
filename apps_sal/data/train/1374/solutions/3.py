t = int(input().strip())
while t:
    (f1, f2, r1, r2, r3, r4) = list(map(int, input().strip().split()))
    (p1, p2, p3, p4) = list(map(float, input().strip().split()))
    x = p1 * (1 - p2) * r2 + p1 * p2 * r1 - f1
    y = p3 * r3 + p3 * p4 * r4 - f2
    if x > y:
        print('FIRST')
    elif x < y:
        print('SECOND')
    else:
        print('BOTH')
    t -= 1
