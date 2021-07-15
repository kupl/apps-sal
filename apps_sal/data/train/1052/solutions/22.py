tl=int(input())
def dsum(n):
    ddsum=0
    while(n!=0):
        a=int(n%10)
        ddsum=ddsum+a
        n=int(n/10)
    return ddsum    
while(tl>0):
    n,d = map(int,input().split(" "))
    i=0
    dic=dict()
    l=[(n,0)]
    while(i<100000 and len(l)!=0):
        t=l.pop(0)
        if(t[0]<10):
            if(t[0] not in dic):
                dic[t[0]]=t[1]
            else:
                continue
        else:
            l.append((dsum(t[0]),t[1]+1))
        l.append((t[0]+d,t[1]+1))
        i+=1
    a=min(dic)
    print(a,dic[a])
    tl=tl-1
