for i in range(int(input())):
    n=int(input())
    a=[int(k) for k in input().split()]
    ind1=0
    ind2=0
    for j in range(len(a)):
        if(a[j]==0):continue
        else:
            ind1=j
            break
    for k in range(len(a)-1,-1,-1):
        if(a[k]==0):continue
        else:
            ind2=k
            break
    #print(ind1,ind2)
    #print(a[ind1:ind2+1])
    print(len(a[ind1:ind2+1]))
