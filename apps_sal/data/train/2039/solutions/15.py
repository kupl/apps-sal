def checker(ij):
    count=0
    for i in range(len(l)):
        #print(count)
        #print(((count-l[i])%m),ij)
        if ((count-l[i])%m)>=ij:
            if l[i]>count:
                count=l[i]
            else:
                return False
    #print(l)
    return True
n,m=input().split()
n,m=[int(n),int(m)]
l=[int(i) for i in input().split()]
beg=-1
last=m
while beg<last-1:
    mid=(beg+last)//2
    counter=checker(mid)
    #print(beg,last)
    if counter:
        last=mid
    else:
        beg=mid
print(beg)

