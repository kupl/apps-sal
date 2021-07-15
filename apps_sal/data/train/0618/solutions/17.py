for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l=l[-(k):]+l
    #print(l)
    c=sum(l[0:k])
    d=sum(l[0:k])
    for i in range(k,len(l)):
        #print(d)
        #print(i,l[i-k],l[i])
        d=(d-l[i-k])+l[i]
        c=max(c,d)
    print(c)

