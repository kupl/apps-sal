t = int(input())
while t > 0:
    k = int(input())
    for i in range(0, k - 1):
        print(' ' * (k - i - 1), end="")
        print('*', end="")
        if(i != 0):
            print(' ' * (2 * i - 1), end="")
            print('*', end="")
        print('\r')
    print('*' * (2 * k - 1))
    t -= 1
