for _ in range(int(input())):
    s = input()
    if s.count('10') + s.count('01') > 2:
        print('non-uniform')
    else:
        print('uniform')
