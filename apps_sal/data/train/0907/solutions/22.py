for _ in range(int(input())):
    n = int(input())
    s = input()
    l = []
    f = True
    for i in range(n):
        if s[i] == 'H':
            l.append(s[i])
        elif s[i] == 'T':
            if len(l) >= 1:
                l = l[:-1]
            else:
                f = False
        if len(l) > 1:
            f = False
    if len(l) > 0:
        f = False
    if f == True:
        print('Valid')
    else:
        print('Invalid')
