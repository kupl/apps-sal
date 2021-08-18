readFromFile = 0
if readFromFile:
    f = open("inputSmall.txt", "r")
    T = int(f.readline())
else:
    T = int(input())

testCases = range(T)

for case in testCases:
    if (readFromFile):
        RC = [int(x) for x in f.readline().split()]
    else:
        RC = [int(x) for x in input().split()]

    R = RC[0]
    C = RC[1]

    aByCols = {}
    aByRows = {}

    uAll = []
    dAll = []
    lAll = []
    rAll = []

    for r in range(R):
        if(readFromFile):
            row = f.readline()
        else:
            row = input()

        for c in range(C):
            if(row[c] == '
                if(r not in aByRows):
                    aByRows[r]=[]
                aByRows[r].append(c)
                if(c not in aByCols):
                    aByCols[c]=[]
                aByCols[c].append(r)

            elif(row[c] == 'U'):
                uAll.append((r, c))

            elif(row[c] == 'D'):
                dAll.append((r, c))

            elif(row[c] == 'L'):
                lAll.append((r, c))

            elif(row[c] == 'R'):
                rAll.append((r, c))

    for x in range(len(uAll)):
        item=uAll[x]
        r=item[0]
        c=item[1]
        if (c in aByCols):
            eaters=aByCols[c]
        else:
            eaters=[]
        age=R
        for y in eaters:
            if (y < r):
                age=min(age, r - y)
        uAll[x]=(item[0], item[1], age)

    for x in range(len(dAll)):
        item=dAll[x]
        r=item[0]
        c=item[1]
        if (c in aByCols):
            eaters=aByCols[c]
        else:
            eaters=[]
        age=R
        for y in eaters:
            if (y > r):
                age=min(age, y - r)
        dAll[x]=(item[0], item[1], age)

    for x in range(len(lAll)):
        item=lAll[x]
        r=item[0]
        c=item[1]
        if (r in aByRows):
            eaters=aByRows[r]
        else:
            eaters=[]
        age=C
        for y in eaters:
            if (y < c):
                age=min(age, c - y)
        lAll[x]=(item[0], item[1], age)

    for x in range(len(rAll)):
        item=rAll[x]
        r=item[0]
        c=item[1]
        if (r in aByRows):
            eaters=aByRows[r]
        else:
            eaters=[]
        age=C
        for y in eaters:
            if (y > c):
                age=min(age, y - c)
        rAll[x]=(item[0], item[1], age)

    uBySum={}
    uByDiff={}
    uByCol={}

    dBySum={}
    dByDiff={}
    dByCol={}

    rBySum={}
    rByDiff={}
    rByRow={}

    lBySum={}
    lByDiff={}
    lByRow={}

    for x in uAll:
        r=x[0]
        c=x[1]
        if (r + c not in uBySum):
            uBySum[r + c]=[]
        if (r - c not in uByDiff):
            uByDiff[r - c]=[]
        if (c not in uByCol):
            uByCol[c]=[]

        uBySum[r + c].append((r, c, x[2]))
        uByDiff[r - c].append((r, c, x[2]))
        uByCol[c].append((r, c, x[2]))

    for x in dAll:
        r=x[0]
        c=x[1]
        if (r + c not in dBySum):
            dBySum[r + c]=[]
        if (r - c not in dByDiff):
            dByDiff[r - c]=[]
        if (c not in dByCol):
            dByCol[c]=[]

        dBySum[r + c].append((r, c, x[2]))
        dByDiff[r - c].append((r, c, x[2]))
        dByCol[c].append((r, c, x[2]))

    for x in lAll:
        r=x[0]
        c=x[1]
        if (r + c not in lBySum):
            lBySum[r + c]=[]
        if (r - c not in lByDiff):
            lByDiff[r - c]=[]
        if (r not in lByRow):
            lByRow[r]=[]

        lBySum[r + c].append((r, c, x[2]))
        lByDiff[r - c].append((r, c, x[2]))
        lByRow[r].append((r, c, x[2]))

    for x in rAll:
        r=x[0]
        c=x[1]
        if (r + c not in rBySum):
            rBySum[r + c]=[]
        if (r - c not in rByDiff):
            rByDiff[r - c]=[]
        if (r not in rByRow):
            rByRow[r]=[]

        rBySum[r + c].append((r, c, x[2]))
        rByDiff[r - c].append((r, c, x[2]))
        rByRow[r].append((r, c, x[2]))

    uSums=set(uBySum.keys())
    uDiffs=set(uByDiff.keys())
    uCols=set(uByCol.keys())
    dSums=set(dBySum.keys())
    dDiffs=set(dByDiff.keys())
    dCols=set(dByCol.keys())
    rSums=set(rBySum.keys())
    rDiffs=set(rByDiff.keys())
    rRows=set(rByRow.keys())
    lSums=set(lBySum.keys())
    lDiffs=set(lByDiff.keys())
    lRows=set(lByRow.keys())

    total=0

    candidates=uSums & lSums
    for cc in candidates:
        r1=[(x[0], 1, x[2]) for x in uBySum[cc]]
        r2=[(x[0], 0, x[2]) for x in lBySum[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if (item[0] - j[0] < j[2]) and (item[0] - j[0] < item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    candidates=dSums & rSums
    for cc in candidates:
        r1=[(x[0], 1, x[2]) for x in rBySum[cc]]
        r2=[(x[0], 0, x[2]) for x in dBySum[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if (item[0] - j[0] < j[2]) and (item[0] - j[0] < item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    candidates=uDiffs & rDiffs
    for cc in candidates:
        r1=[(x[0], 1, x[2]) for x in uByDiff[cc]]
        r2=[(x[0], 0, x[2]) for x in rByDiff[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if (item[0] - j[0] < j[2]) and (item[0] - j[0] < item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    candidates=dDiffs & lDiffs
    for cc in candidates:
        r1=[(x[0], 1, x[2]) for x in lByDiff[cc]]
        r2=[(x[0], 0, x[2]) for x in dByDiff[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if (item[0] - j[0] < j[2]) and (item[0] - j[0] < item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    candidates=dCols & uCols
    for cc in candidates:
        r1=[(x[0], 1, x[2]) for x in uByCol[cc]]
        r2=[(x[0], 0, x[2]) for x in dByCol[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if ((item[0] - j[0]) % 2 == 0) and (item[0] - j[0] < 2 * j[2]) and (item[0] - j[0] < 2 * item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    candidates=lRows & rRows
    for cc in candidates:
        r1=[(x[1], 1, x[2]) for x in lByRow[cc]]
        r2=[(x[1], 0, x[2]) for x in rByRow[cc]]
        rTot=r1 + r2
        rTot.sort()

        zeros=[]
        for i in range(len(rTot)):
            item=rTot[i]
            if (item[1] == 1):
                for j in zeros:
                    if ((item[0] - j[0]) % 2 == 0) and (item[0] - j[0] < 2 * j[2]) and (item[0] - j[0] < 2 * item[2]):
                        total=total + 1
            elif (item[1] == 0):
                zeros.append(item)

    print(total)
