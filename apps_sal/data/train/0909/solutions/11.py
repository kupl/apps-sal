import re
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))
    a = sorted(b)
    b = sorted(g)
    (i, j) = (0, 0)
    x = ''
    cutt = 2
    while i < n and j < n:
        if a[i] < b[j]:
            x += 'b'
            i += 1
        elif a[i] == b[j]:
            if len(x) == 0:
                x += 'b'
                cutt = 1
                i += 1
            elif x[-1] == 'b':
                x += 'g'
                j += 1
            else:
                x += 'b'
                i += 1
        else:
            x += 'g'
            j += 1
    while i < n:
        x += 'b'
        i += 1
    while j < n:
        x += 'g'
        j += 1
    w = re.findall('[b]{2}', x)
    t = re.findall('[g]{2}', x)
    if (w or t) and cutt == 1:
        i = 0
        n = len(a)
        j = 0
        x = ''
        while i < n and j < n:
            if a[i] < b[j]:
                x += 'b'
                i += 1
            elif a[i] == b[j]:
                if len(x) == 0:
                    x += 'g'
                    j += 1
                elif x[-1] == 'b':
                    x += 'g'
                    j += 1
                else:
                    x += 'b'
                    i += 1
            else:
                x += 'g'
                j += 1
        while i < n:
            x += 'b'
            i += 1
        while j < n:
            x += 'g'
            j += 1
        w = re.findall('[b]{2}', x)
        t = re.findall('[g]{2}', x)
        if w or t:
            print('NO')
        else:
            print('YES')
    elif w or t:
        print('NO')
    else:
        print('YES')
