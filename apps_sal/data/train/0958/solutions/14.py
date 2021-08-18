t = int(input())
for _ in range(t):
    a = int(input())
    if(a == 1):
        print('*')
    else:
        print(' ' * (a - 1), end="")
        print('*')
        j = 1
        for i in range(2, a):
            print(' ' * (a - i), end="")
            print('*', end="")
            print(' ' * ((2 * (j)) - 1), end="")
            print('*', end="")
            print()
            j += 1
        print('*' * (2 * a - 1))
