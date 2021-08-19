for t in range(int(input())):
    a = input()
    if a.count('10') + a.count('01') > 2:
        print('non-uniform')
    else:
        print('uniform')
