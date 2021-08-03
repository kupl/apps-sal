# cook your code here
t = eval(input())
for i in range(t):
    f1, f2, r1, r2, r3, r4 = list(map(int, input().split()))
    p1, p2, p3, p4 = list(map(float, input().split()))
    x = p1 * p2
    y = p1 * (1 - p2)
    a1 = (x * r1 + y * r2) - f1
    a2 = (r3 * p3 + r4 * p3 * p4) - f2
    if a1 > a2:
        print('FIRST')
    elif a2 > a1:
        print('SECOND')
    else:
        print('BOTH')
