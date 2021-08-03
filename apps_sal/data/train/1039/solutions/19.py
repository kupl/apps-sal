list = []
for i in range(int(input())):
    X, Y = map(int, input().split())
    x = Y - X
    op = 0
    if x == 0:
        op = 0
    elif x > 0:
        if x % 2 != 0:
            op = 1
        elif x % 4 == 0:
            op = 3
        else:
            op = 2
    elif x < 0:
        if x % 2 != 0:
            op = 2
        else:
            op = 1
    list.append(op)
for l in list:
    print(l)
