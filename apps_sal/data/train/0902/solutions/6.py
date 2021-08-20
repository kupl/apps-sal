for _ in range(int(input())):
    (n, s) = input().split()
    n = int(n)
    b = []
    for i in range(n):
        b.append(input())
    zero = 0
    one = 0
    for i in range(n):
        if b[i][0] == '0':
            zero += b[i].count('0')
        else:
            one += b[i].count('1')
    if s == 'Dee':
        if zero > one:
            print('Dee')
        else:
            print('Dum')
    elif one > zero:
        print('Dum')
    else:
        print('Dee')
