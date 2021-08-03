a = list(input())
if a[0] == 'f':
    print('ftp://', end='')
    a = a[3:]
    while len(a[:''.join(a).index('ru')]) == 0:
        if len(a[:''.join(a).index('ru')]) != 0:
            print(''.join(a[:''.join(a).index('ru')]), end='')
        else:
            print('ru', end='')
            a = a[''.join(a).index('ru') + 2:]
    print(''.join(a[:''.join(a).index('ru')]), end='')
    a = a[''.join(a).index('ru') + 2:]
    print('.ru', end='')
    if len(a) != 0:
        print('/', end='')
        print(''.join(a))
else:
    print('http://', end='')
    a = a[4:]
    while len(a[:''.join(a).index('ru')]) == 0:
        if len(a[:''.join(a).index('ru')]) != 0:
            print(''.join(a[:''.join(a).index('ru')]), end='')
        else:
            print('ru', end='')
            a = a[''.join(a).index('ru') + 2:]
    print(''.join(a[:''.join(a).index('ru')]), end='')
    a = a[''.join(a).index('ru') + 2:]
    print('.ru', end='')
    if len(a) != 0:
        print('/', end='')
        print(''.join(a))
