for testcases in range(int(input())):
    (x, y) = map(int, input('').split())
    z = y - x
    if z == 0:
        print(0)
    elif z > 0:
        if z % 2 == 0:
            z /= 2
            if z % 2 == 0:
                print(3)
            else:
                print(2)
        else:
            print(1)
    elif z % 2 == 0:
        print(1)
    else:
        print(2)
