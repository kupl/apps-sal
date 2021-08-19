try:
    t = int(input())
    for i in range(0, t):
        n = int(input())
        flist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        glist = []
        hlist = []
        for j in range(0, len(flist)):
            for k in range(j + 1, len(flist)):
                glist.append(flist[j] * flist[k])
        for h in range(0, len(glist)):
            for f in range(h, len(glist)):
                hlist.append(glist[h] + glist[f])
        hlist.sort()
        if n in hlist:
            print('YES')
        else:
            print('NO')
except:
    pass
