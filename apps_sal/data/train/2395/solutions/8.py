for tc in range(int(input())):
    n = int(input())
    s = input()
    ch = 0
    a = ''
    b = ''
    for c in s:
        if c == '2':
            if ch:
                a += '0'
                b += '2'
            else:
                a += '1'
                b += '1'
        elif c == '1':
            if ch:
                a += '0'
                b += '1'
            else:
                ch = 1
                a += '1'
                b += '0'
        else:
            a += '0'
            b += '0'
    print(a)
    print(b)
