t = int(input())
for i in range(0, t):
    (f1, f2, r1, r2, r3, r4) = list(map(int, input().split()))
    (p1, p2, p3, p4) = list(map(float, input().split()))
    a1 = p1 * (r1 * p2 + r2 * (1 - p2)) - f1
    a2 = p3 * r3 + p3 * r4 * p4 - f2
    if a1 > a2:
        print('FIRST')
    elif a1 < a2:
        print('SECOND')
    else:
        print('BOTH')
