for i in range(int(input())):
    x, y = list(map(int, input().split()))
    if y > x:
        if (x - y) % 4 == 0:
            print("3")
        elif (x - y) % 2 == 0:
            print("2")
        else:
            print("1")
    elif x > y:
        if (y - x) % 2 == 0:
            print("1")
        else:
            print("2")
    else:
        print("0")
