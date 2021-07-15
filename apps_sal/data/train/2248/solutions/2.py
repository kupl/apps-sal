import sys
input = sys.stdin.readline
for f in range(int(input())):
    p,q=list(map(int,input().split()))
    d=2
    facs=[]
    facsm=[]
    while q>=d*d:
        if q%d==0:
            facs.append(d)
            x=0
            while q%d==0:
                x+=1
                q//=d
            facsm.append(x-1)
        d+=1
    if q>1:
        facs.append(q)
        facsm.append(0)
    mc=p
    pc=p
    for i in range(len(facs)):
        x=0
        while pc%facs[i]==0:
            x+=1
            pc//=facs[i]
        mc=min(mc,facs[i]**(x-min(x,facsm[i])))
    p//=mc
    print(p)

