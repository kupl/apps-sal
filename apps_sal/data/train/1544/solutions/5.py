for _ in range(int(input())):
    n = int(input())
    a = 0
    if n == 1:
        print('*')
    elif n == 2:
        print('*')
        print('**')
    else:
        print('*')
        for _ in range(2, n):
            print('*', end="")
            if a > 0:
                print(' ' * a, end="")
            a += 1
            print('*')
        print('*' * n)
