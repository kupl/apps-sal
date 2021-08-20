t = int(input())
for i in range(0, t):
    (x1, x2, x3, x4) = list(map(int, input().split()))
    z = x1 * x1 + x2 * x2
    z1 = x3 * x3 + x4 * x4
    if z > z1:
        print('B IS CLOSER')
    else:
        print('A IS CLOSER')
