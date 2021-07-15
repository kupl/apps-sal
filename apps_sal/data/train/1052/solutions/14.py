def digitsum(n):
    s=0
    while n:
        s=s+n%10
        n=n//10
    return(s)
x=int(input())
for i in range(x):
    a,b=input().split()
    a,b=[int(a),int(b)]
    l1=[(a,0)]
    l2={}
    i=0
    while i<10000 and len(l1)!=0:
        first=l1.pop(0)
        if first[0]<10:
            if first[0] not in l2:
                l2[first[0]]=first[1]
        else:
            l1.append((digitsum(first[0]),first[1]+1))
        l1.append((first[0]+b,first[1]+1))
        i+=1
    a=min(l2)
    print(a,l2[a])
