for _ in range(int(input())):
    x,y=map(int,input().split())
    if(x==y):
        if(x==1):
            print(1)
        else:
            n=0
            for i in range(x-1):
                n=i
                for _ in range(y):
                    print(n,end=' ')
                    n=(n+1)%x
                print()  
            for i in range(x):
                print(i,end=' ')
            print( )
    else:
        l=[]
        n=min(x,y)
        m=max(x,y)
        for _ in range(n):
            l.append([])
        v=n+1
        for i in range(n):
            u=i
            for j in range(m):
                if(j<=n):
                    l[i].append(u)
                    u=(u+1)%(n+1)
                else:
                    if(j>=v):
                        l[i].append(j+1)
                    else:
                        l[i].append(j)
            v=v+1
        if(x>y):
            for i in range(x):
                for j in l:
                    print(j[i],end=' ')
                print( )
        else:
            for i in l:
                for j in i:
                    print(j,end=' ')
                print( )
