for i in range(int(input())):
    n = input()
    tmp = n.split(' ')
    if 'not' in tmp:
        print('Real Fancy')
    else:
        print('regularly fancy')
