try:
    t=int(input())
    ans=[]
    while(t>0):
        t-=1
        li=list(map(int,input().split()))
        a=li[0]
        d=li[1]
        k=li[2]
        n=li[3]
        inc=li[4]
        for i in range(1,n):
            if((i)%k==0):
                d=d+inc
            a=a+d
        ans.append(a)
    for i in ans:
        print(i)
except:
    pass

