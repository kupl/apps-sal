for i in range(int(input())):
    n = input()
    t = n.count('10') + n.count('01')
    if(n[-1] != n[0]):
        t += 1
    print('uniform' if t <= 2 else 'non-uniform')
