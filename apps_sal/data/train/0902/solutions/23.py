for t in range(int(input())):
    (n, m) = [x for x in input().split()]
    a = int(n)
    (n0, n1) = (0, 0)
    for i in range(a):
        s = input()
        z = s[0]
        if z == '0':
            n0 += 1
        else:
            n1 += 1
        for i in range(1, len(s)):
            if s[i] == s[0]:
                if s[i] == '0':
                    n0 += 1
                if s[i] == '1':
                    n1 += 1
    if n0 == n1:
        if m == 'Dee':
            print('Dum')
        if m == 'Dum':
            print('Dee')
    if n0 > n1:
        print('Dee')
    if n1 > n0:
        print('Dum')
