for _ in range(int(input())):
    a = list(input())
    for i in range(len(a) - 1):
        if a[i] == 's':
            if a[i + 1] == 'm':
                a[i] = 'd'
                a[i + 1] = 'e'
        elif a[i] == 'm':
            if a[i + 1] == 's':
                a[i + 1] = 'd'
                a[i] = 'e'
    votes = 0
    for creature in a:
        if creature == 'm' or creature == 'e':
            votes += 1
        elif creature == 's':
            votes -= 1
    if votes > 0:
        print('mongooses')
    elif votes < 0:
        print('snakes')
    else:
        print('tie')
