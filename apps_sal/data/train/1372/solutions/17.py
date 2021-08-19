t = int(input())
for i in range(0, t):
    (x, y, x1, y1) = list(map(int, input().split()))
    w = ((x - 0) ** 2 + (y - 0) ** 2) ** (1 / 2)
    e = ((x1 - 0) ** 2 + (y1 - 0) ** 2) ** (1 / 2)
    if w > e:
        print('B IS CLOSER')
    else:
        print('A IS CLOSER')
