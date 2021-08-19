def more_zeros(s):
    L = []
    L1 = []
    L2 = []
    for i in s:
        a = int(' '.join((format(ord(x), 'b') for x in i)))
        for j in str(a):
            if j == '0':
                L1.append(j)
            else:
                L2.append(j)
        if len(L1) > len(L2):
            if i not in L:
                L.append(str(i))
        L1 = []
        L2 = []
    return L
