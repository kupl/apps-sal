try:
    for i in range(int(input())):
        s = input()
        d = s.find('W')
        l = d - 0
        r = len(s) - 1 - d
        if r == l:
            print('Chef')
        else:
            print('Aleksa')
except:
    pass
