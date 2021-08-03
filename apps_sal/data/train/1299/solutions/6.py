# cook your dish here
try:
    for _ in range(int(input())):
        s1 = int(input())
        po = list(map(int, input().split()))
        yp = set(po)
        mo = []
        sa = [po[0]]
        da = []
        for x in yp:
            mo.append(x)
        mo.sort()
        bun = 0
        cop = po[0]
        for x in range(1, len(po)):
            if(po[x] != cop or x - bun > 1):
                sa.append(po[x])
                bun = x
                cop = po[x]
        for x in range(len(mo)):
            da.append(sa.count(mo[x]))
        daa = da.index(max(da))
        print(mo[daa])
except:
    pass
