try:
    for i in range(int(input())):
        a = int(input())
        b = str(a)
        c = list(b)
        for i in range(len(c)):
            c[i] = int(c[i])
        ab = []
        for i in c:
            i = i - 2
            ab.append(i)
        for i in ab:
            print(i, end='')
        print('')
except:
    pass
