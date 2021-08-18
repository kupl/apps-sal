for i in range(int(input())):
    count = 0
    for j in range(int(input())):
        XY = input().split()
        X = int(XY[0])
        Y = int(XY[1])
        if Y - X > 5 or X - Y > 5:
            count += 1
    print(count)
