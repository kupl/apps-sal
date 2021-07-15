for f in range(int(input())):
    n=int(input())
    segs=[[n,0]]
    sol=[0]*n
    i=0
    prev=n
    j=0
    while i<n:
        i+=1
        if j<0:
            segs.sort(reverse=True)
            j=0
            while j<len(segs) and segs[j][0]==segs[j+1][0]:
                j+=1
            prev=segs[0][0]
        m=segs[j][1]+(segs[j][0]-1)//2
        sol[m]=i
        segs.append([segs[j][0]//2,m+1])
        segs.append([(segs[j][0]-1)//2,segs[j][1]])
        segs[j][0]=0
        j-=1
    print(*sol)
