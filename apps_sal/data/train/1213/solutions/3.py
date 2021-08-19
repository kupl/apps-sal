t = int(input())
for i in range(t):
    (x1, x2, x3, v1, v2) = list(map(int, input().split()))
    a = x1 - x3
    b = x3 - x1
    if a < b:
        a = b
    else:
        b = a
    A = x2 - x3
    B = x3 - x2
    if A < B:
        A = B
    else:
        B = A
    c = a / v1
    d = A / v2
    if c < d:
        print('Chef')
    elif c > d:
        print('Kefa')
    else:
        print('Draw')
