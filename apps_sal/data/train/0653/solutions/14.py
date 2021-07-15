try:
    n=int(input())
    li=list(map(int,input().split()))
    l=int(input())
    p=0
    m=0
    k=len(li)-1
    li.sort()
    i=0
    while(i<=k):
        if l>=li[i]:
            l-=li[i]
            p+=1
            i+=1
            if m<p:
                m=p
        else:
            if p>0:
                l+=li[k]
                p-=1
                li.pop(k)
                k-=1
            else:
                break
    print(m)
except:
    pass
