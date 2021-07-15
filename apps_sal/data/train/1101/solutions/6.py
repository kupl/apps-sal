t=int(input())
for t1 in range(t):
    n,c,k1=(int(i) for i in input().split())
    #print(n,c,k1)
    lis=[dict([]) for i in range(c+1)]
    ma=1
    for i in range(n):
        x=[int(j) for j in input().split()]
        if x[0] in lis[x[2]]:
            lis[x[2]][x[0]]+=1
        else:
            lis[x[2]][x[0]]=1
        ma=max(ma,lis[x[2]][x[0]])
    de=[int(i) for i in input().split()]
    if ma==1:
        kna=[[0 for i in range(k1+1)],[0 for i in range(k1+1)]]
        ct=0
        tot=0
        for i in range(1,c+1) :
            k=len(lis[i])
            v=de[i-1]
            tot+=(k*(k-1)*(k-2))/6
            for j in range(1,len(lis[i])-1):
                be=ct%2
                no=(be+1)%2
                val=((k-j)*(k-j-1))/2
                for z in range(k1+1):
                    if z>=v :
                        kna[no][z]=max(kna[be][z],kna[be][z-v]+val)
                    else:
                        kna[no][z]=kna[be][z]
                ct+=1
        tot=tot-max(kna[0][k1],kna[1][k1])
        print(int(tot))
    else:
        kna=[[0 for i in range(k1+1)],[0 for i in range(k1+1)]]
        ct=0
        tot=0
        for i in range(1,c+1):
            nlist=[lis[i][j] for j in lis[i]]
            nlist.sort()
            k=len(nlist)
            v=de[i-1]
            su=0
            tri=0
            for j in range(k-3,-1,-1) :
                su+=nlist[j+2]
                tri+=su*nlist[j+1]
                tot+=tri*nlist[j]
                val=tri
                for z1 in range(nlist[j]):
                    be=ct%2
                    no=(be+1)%2
                    for z in range(k1+1):
                        if z>=v :
                            kna[no][z]=max(kna[be][z],kna[be][z-v]+val)
                        else:
                            kna[no][z]=kna[be][z]
                    ct+=1
                #print(kna[no][k1])
        tot=tot-max(kna[0][k1],kna[1][k1])
        print(int(tot))
