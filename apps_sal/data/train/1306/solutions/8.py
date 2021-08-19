t = int(input())
for _ in range(t):
    s = input()
    d = {}
    for i in s:
        try:
            d[i] += 1
        except:
            d[i] = 1
    if len(s) < 5:
        print('NO')
    elif len(s) == 5:
        s = sorted(s)
        if ''.join(s) == 'EILMT':
            print('YES')
        else:
            print('NO')
    else:
        a = 0
        s = sorted(s)
        if ''.join(s) == 'EIILLMMTT':
            print('YES')
        else:
            k = 'LTIME'
            a = 0
            for j in k:
                try:
                    x = d[j]
                    if x >= 2:
                        a += 1
                except:
                    pass
            if a == 5:
                print('YES')
            else:
                print('NO')
