for _ in range(int(input())):
    n = int(input())
    number = input()
    a = []
    b = []
    flag = 0
    for c in number:
        if c == '2':
            if flag == 0:
                a.append('1')
                b.append('1')
            else:
                b.append('2')
                a.append('0')
        elif c == '0':
            a.append('0')
            b.append('0')
        elif flag == 0:
            a.append('1')
            b.append('0')
            flag = 1
        else:
            a.append('0')
            b.append('1')
    print(''.join(a))
    print(''.join(b))
