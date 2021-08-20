def f():
    (f1, f2, r1, r2, r3, r4) = list(map(int, input().split()))
    (p1, p2, p3, p4) = list(map(float, input().split()))
    e1 = p1 * (p2 * r1 + (1 - p2) * r2) - f1
    e2 = p3 * (p4 * r4 + r3) - f2
    if e1 == e2:
        return 'BOTH'
    if e1 > e2:
        return 'FIRST'
    return 'SECOND'


t = int(input())
for i in range(t):
    print(f())
