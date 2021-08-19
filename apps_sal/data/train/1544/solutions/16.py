for a0 in range(int(input())):
    n = int(input())
    if n == 1:
        print('*')
    elif n == 2:
        print('*')
        print('**')
    elif n == 3:
        print('*')
        print('**')
        print('***')
    else:
        print('*')
        print('**')
        for i in range(3, n):
            s = ' ' * (i - 2)
            print('*' + s + '*')
        print('*' * n)
