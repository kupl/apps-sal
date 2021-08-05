chakra = 0
t = eval(input())
for a in range(0, t):
    chakra = 0
    s = input()
    l = s.split()
    n = int(l[0])
    m = int(l[1])
    lnew = []
    soint = []
    sofloat = []
    for i in range(0, n):
        s = input()
        l = s.split()
        soint += [[int(l[0]), int(l[1])]]
    for i in range(0, m):
        s = input()
        l = s.split()
        sofloat += [[int(l[0]), int(l[1])]]
    for i in range(0, n):
        sumi = 0
        sumf = 0
        if not(soint[i][1] in lnew):
            lnew += [soint[i][1]]
            for j in range(i, n):
                if soint[i][1] == soint[j][1]:
                    sumi += soint[j][0]
            for k in range(0, m):
                if soint[i][1] == sofloat[k][1]:
                    sumf += sofloat[k][0]
            if sumi <= sumf:
                chakra += sumf - sumi
    print(chakra)
