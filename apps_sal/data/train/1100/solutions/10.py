for _ in range(int(input())):
    p,q,r=list(map(int,input().split()))
    a,b,c=list(map(int,input().split()))
    l=[]
    l.append(a-p)
    l.append(b-q)
    l.append(c-r)
    ans=3
    ans-=l.count(0)
    for i in l:
        if i<0:
            print(-1)
            break
    else:
        print(sum(l))

