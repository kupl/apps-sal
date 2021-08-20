for _ in range(int(input())):
    (n, t) = input().split()
    n = int(n)
    one = 0
    zero = 0
    for i in range(n):
        s = input()
        if s[0] == '1':
            one += s.count('1')
        else:
            zero += s.count('0')
    if one > zero:
        print('Dum')
    elif one < zero:
        print('Dee')
    elif t == 'Dee':
        print('Dum')
    else:
        print('Dee')
