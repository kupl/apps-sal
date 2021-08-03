try:
    for i in range(int(input())):
        s = input()
        d = s.find('W')
        l = d - 0
        # print(l)
        r = (len(s) - 1) - d
        # print(r)
        if(r == l):
            print('Chef')
        else:
            print('Aleksa')
except:
    pass
