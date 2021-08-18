for i in range(0, int(input())):
    power, x, y, z = list(map(float, input().split()))
    summ = x + y + z
    a = x + y
    b = y + z
    flagg = 0
    if(x == y and y == z):
        flagg == 0

    else:
        flagg = 0

    if(power >= summ):
        print('1')
    else:
        if(flagg == 1):
            if((x + y) >= power):
                print('2')
            else:
                print('3')
        else:

            if((power - z) >= y):

                print('2')

            else:
                if((power - y) >= x):
                    print('2')
                else:
                    print('3')
