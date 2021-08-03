for i in range(int(input())):
    a = input()
    c = a.count('m')
    d = a.count('s')
    t = 0
    while t < len(a) - 1:
        if (a[t] == 'm' and a[t + 1] == 's') or (a[t] == 's' and a[t + 1] == 'm'):
            d = d - 1
            t = t + 2
        else:
            t = t + 1
    if c > d:
        print('mongooses')
    elif d > c:
        print('snakes')
    else:
        print('tie')
