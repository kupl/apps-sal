t = int(input())
while t:
    s = input()
    f = 1
    for i in 'MITL':
        if s.count(i) < 2:
            f = 0
            break
    if f:
        if len(s) == 9:
            if s.count('E'):
                print('YES')
            else:
                print('NO')
        elif s.count('E') > 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    t -= 1
