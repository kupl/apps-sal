for t in range(int(input())):
    x, y = map(int, input().split())
    z = x - y
    if x > y:
        if z % 2 == 0:
            print(1)
        else:
            print(2)
    elif x < y:
        if z % 2 != 0:
            print(1)
        elif z % 4 == 0:
            print(3)
        else:
            print(2)
    else:
        print(0)
