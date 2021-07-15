def nQueen(n):   
    if n==2 or n==3:
        return []
    r=n%12
    L=[2*i for i in range(1,n//2+1)]
    if r==3 or r==9:
        L=L[1:]+[2]
    if n%2==0:
        L1=[2*i-1 for i in range(1,n//2+1)]
    else:
        L1=[2*i-1 for i in range(1,n//2+2)]

    if r==8:
        for i in range(1,len(L1),2):
            L1[i-1],L1[i]=L1[i],L1[i-1]
    if r==2:
        L1[0],L1[1]=L1[1],L1[0]
        L1.remove(5)
        L1.append(5)
    if r==3 or r==9:
        L1.remove(1)
        L1.append(1)
        L1.remove(3)
        L1.append(3)
    L=L+L1
    return [t-1 for t in L]
