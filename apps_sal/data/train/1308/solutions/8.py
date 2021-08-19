def password():
    while True:
        st = input()
        ls = list(st)
        ln = len(st)
        c = 0
        fl = 0
        for i in range(0, ln):
            if ord(ls[i]) <= 122 and ord(ls[i]) >= 97:
                c = 1
            elif ls[i].isdigit():
                fl = 1
        a = 1
        for i in range(0, ln - 1):
            for j in range(i + 1, ln):
                if ls[i] == ls[j]:
                    a = a + 1
        if c == 1 and fl == 1 and (a == 1):
            print('\nValid')
            break
        else:
            print('\nInvalid')


password()
