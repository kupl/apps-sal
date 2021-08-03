for i in range(int(input())):
    yy = input()
    y = [int(e) for e in yy.split()]
    zz = input()
    z = [int(e) for e in zz.split()]
    count = 0
    for i in z:
        a = i + y[1]
        if a % 7 == 0:
            count += 1
    print(count)
