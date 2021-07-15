for _ in range(int(input())):
    l=list(map(int,input().split()))
    k=list(map(int,input().split()));f=0
    for i in range(len(l)):
        p=k[i]-l[i]
        if p<0:
            f=-1;break
        else:
            f+=p
    print(f)
