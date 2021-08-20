t = int(input())
while t:
    (n, s) = input().split()
    n = int(n)
    Deec = 0
    Dumc = 0
    b = []
    for _ in range(n):
        x = input()
        if x[0] == '0':
            for i in x:
                if i == '0':
                    Deec += 1
        if x[0] == '1':
            for i in x:
                if i == '1':
                    Dumc += 1
    if s == 'Dee':
        if Deec > Dumc:
            print('Dee')
        else:
            print('Dum')
    elif Dumc > Deec:
        print('Dum')
    else:
        print('Dee')
    t -= 1
