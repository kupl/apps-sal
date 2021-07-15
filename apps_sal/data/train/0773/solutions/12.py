
T = int(input())

while (T > 0):
    T-=1 
    k = int(input())
    perm = []
    if k % 2 == 0:
        for i in range(2,k+1,2):
            perm.append(i)
            perm.append(i-1)
    else:
        r = k - 3
        for i in range(2,k-2,2):
            perm.append(i)
            perm.append(i-1)
        perm.extend( [k-1,k,k-2] )
    for i in perm:
        print(i,end=' ')
    print()
        

