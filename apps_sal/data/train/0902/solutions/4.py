for i in range(int(input())):
    (a, string) = input().split()
    zero = 0
    one = 0
    for j in range(0, int(a)):
        k = input()
        if k[0] == '1':
            one += k.count('1')
        else:
            zero += k.count('0')
    if string == 'Dum':
        if one > zero:
            print('Dum')
        else:
            print('Dee')
    elif zero > one:
        print('Dee')
    else:
        print('Dum')
